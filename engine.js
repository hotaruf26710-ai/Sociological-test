/**
 * Socius Trace Core Engine v2
 * 四轴向量计算 + 按时代分组欧氏距离匹配
 */

// ─── 归一化用户向量 ─────────────────────────────────────────────

function calculateUserVector(userAnswers, questions) {
  const axes = ['scale', 'force', 'order', 'stance'];
  const rawScores = { scale: 0, force: 0, order: 0, stance: 0 };
  const maxScores = { scale: 0, force: 0, order: 0, stance: 0 };

  questions.forEach(q => {
    axes.forEach(axis => {
      const maxPossible = Math.max(...q.options.map(opt => Math.abs(opt.effects[axis] || 0)));
      maxScores[axis] += maxPossible;
    });
  });

  userAnswers.forEach(ans => {
    const question = questions.find(q => q.id === ans.questionId);
    if (!question) return;
    const selectedEffect = question.options[ans.optionIndex].effects;
    axes.forEach(axis => {
      rawScores[axis] += (selectedEffect[axis] || 0);
    });
  });

  return [
    maxScores.scale === 0 ? 0 : rawScores.scale / maxScores.scale,
    maxScores.force === 0 ? 0 : rawScores.force / maxScores.force,
    maxScores.order === 0 ? 0 : rawScores.order / maxScores.order,
    maxScores.stance === 0 ? 0 : rawScores.stance / maxScores.stance
  ];
}

// ─── 欧氏距离 → 匹配度% ─────────────────────────────────────────

function distanceToMatch(dist) {
  // 四维空间中最大可能欧氏距离 = sqrt(4 * 2^2) = 4
  const maxDist = 4;
  return Math.round((1 - Math.min(dist, maxDist) / maxDist) * 100);
}

// ─── 按时代分组匹配 ──────────────────────────────────────────────

function findMatchingScholars(userVector, scholars) {
  const withDistance = scholars.map(scholar => {
    const sumOfSquares = userVector.reduce((sum, val, i) => {
      return sum + Math.pow(val - scholar.vector[i], 2);
    }, 0);
    return {
      ...scholar,
      distance: Math.sqrt(sumOfSquares),
      matchPct: distanceToMatch(Math.sqrt(sumOfSquares))
    };
  });

  // 按时代分组，各取 Top 1
  const eras = ['古典', '现代', '当代'];
  const byEra = {};
  eras.forEach(era => {
    const group = withDistance.filter(s => s.era === era);
    group.sort((a, b) => a.distance - b.distance);
    byEra[era] = group; // 保存全组，UI 可用 [0] 取最近
  });

  // 全局排序用于散点图着色
  withDistance.sort((a, b) => a.distance - b.distance);

  return { byEra, all: withDistance };
}

// ─── ECharts 雷达图配置（暗色主题，无需注册 'dark'）──────────────

function getRadarOptions(userVector, scholarVector, scholarName) {
  const mapTo100 = (val) => ((val + 1) / 2) * 100;
  const DARK = '#888888';
  const GRID = '#2e2e2e';

  return {
    backgroundColor: 'transparent',
    textStyle: { color: DARK },
    tooltip: { trigger: 'item', backgroundColor: '#1a1a1a', borderColor: '#2e2e2e', textStyle: { color: '#fff' } },
    legend: {
      data: ['你的坐标', scholarName],
      bottom: 4,
      textStyle: { fontSize: 11, color: DARK }
    },
    radar: {
      indicator: [
        { name: 'Scale\n微观 ↔ 宏观', max: 100 },
        { name: 'Force\n物质 ↔ 符号', max: 100 },
        { name: 'Order\n和谐 ↔ 冲突', max: 100 },
        { name: 'Stance\n解释 ↔ 批判', max: 100 }
      ],
      center: ['50%', '48%'],
      radius: '62%',
      shape: 'polygon',
      axisName: { color: '#999999', fontWeight: '700', fontSize: 10 },
      splitArea: { areaStyle: { color: ['rgba(99,102,241,0.04)', 'rgba(99,102,241,0.08)'] } },
      axisLine: { lineStyle: { color: GRID } },
      splitLine: { lineStyle: { color: GRID } }
    },
    series: [{
      type: 'radar',
      data: [
        {
          value: userVector.map(mapTo100),
          name: '你的坐标',
          itemStyle: { color: '#6366f1' },
          areaStyle: { opacity: 0.2, color: '#6366f1' },
          lineStyle: { color: '#6366f1', width: 2 }
        },
        {
          value: scholarVector.map(mapTo100),
          name: scholarName,
          itemStyle: { color: '#f43f5e' },
          areaStyle: { opacity: 0.08, color: '#f43f5e' },
          lineStyle: { type: 'dashed', color: '#f43f5e', width: 2 }
        }
      ]
    }]
  };
}

// ─── ECharts 散点图配置（暗色主题）──────────────────────────────

function getScatterOptions(userVector, allScholars) {
  const eraColors = { '古典': '#f59e0b', '现代': '#60a5fa', '当代': '#34d399' };
  const DARK = '#666666';
  const GRID = '#2e2e2e';

  const seriesMap = {};
  allScholars.forEach(s => {
    if (!seriesMap[s.era]) {
      seriesMap[s.era] = {
        name: s.era,
        type: 'scatter',
        symbolSize: 12,
        itemStyle: { color: eraColors[s.era] },
        label: {
          show: true,
          formatter: p => p.data[2],
          position: 'top',
          fontSize: 9,
          color: eraColors[s.era]
        },
        data: []
      };
    }
    seriesMap[s.era].data.push([s.vector[0], s.vector[3], s.nameEn || s.name]);
  });

  return {
    backgroundColor: 'transparent',
    textStyle: { color: DARK },
    tooltip: {
      backgroundColor: '#1a1a1a', borderColor: '#2e2e2e', textStyle: { color: '#fff' },
      formatter: p => `<b>${p.data[2]}</b><br/>Scale: ${p.data[0].toFixed(2)}<br/>Stance: ${p.data[1].toFixed(2)}`
    },
    legend: {
      data: ['古典', '现代', '当代', '你'],
      bottom: 4,
      textStyle: { fontSize: 10, color: DARK }
    },
    grid: { left: 52, right: 24, top: 24, bottom: 40 },
    xAxis: {
      name: '← 微观  Scale  宏观 →',
      nameLocation: 'center', nameGap: 26,
      nameTextStyle: { color: DARK, fontSize: 10 },
      min: -1.3, max: 1.3,
      axisLine: { show: true, lineStyle: { color: '#ffffff', width: 2 } },
      axisTick: { show: false },
      splitLine: { lineStyle: { type: 'dashed', color: GRID } },
      axisLabel: { show: false }
    },
    yAxis: {
      name: '← 解释  Stance  批判 →',
      nameLocation: 'center', nameGap: 40,
      nameTextStyle: { color: DARK, fontSize: 10 },
      min: -1.3, max: 1.3,
      axisLine: { show: true, lineStyle: { color: '#ffffff', width: 2 } },
      axisTick: { show: false },
      splitLine: { lineStyle: { type: 'dashed', color: GRID } },
      axisLabel: { show: false }
    },
    series: [
      ...Object.values(seriesMap),
      {
        name: '你',
        type: 'scatter',
        symbolSize: 20,
        symbol: 'pin',
        itemStyle: { color: '#6366f1' },
        label: {
          show: true, formatter: '你',
          position: 'top', fontWeight: 'bold', fontSize: 10, color: '#818cf8'
        },
        data: [[userVector[0], userVector[3], '你']]
      }
    ]
  };
}
