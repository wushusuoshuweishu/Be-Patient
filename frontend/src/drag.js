export function dragBox (drag, wrap) {//drag可拖内容，wrap外层包装
    function getCss (ele, prop) {
      return parseInt(window.getComputedStyle(ele)[prop])
    }
    let initX;
    let initY;
    let dragable = false;
    let wrapLeft = getCss(wrap, 'left');
    let wrapRight = getCss(wrap, 'top');
    drag.addEventListener('mousedown', function (e) {//鼠标按下
      dragable = true;
      initX = e.clientX;
      initY = e.clientY;
    }, false);
    document.addEventListener('mousemove', function (e) {//鼠标移动
      if (dragable === true) {
        let nowX = e.clientX;
        let nowY = e.clientY;
        let disX = nowX - initX;
        let disY = nowY - initY;
        wrap.style.left = wrapLeft + disX + 'px';//位置和按下时位置对的偏差即变化后量
        wrap.style.top = wrapRight + disY + 'px';
      }
    });
    drag.addEventListener('mouseup', function (e) {//鼠标按下起来
      dragable = false;
      wrapLeft = getCss(wrap, 'left');
      wrapRight = getCss(wrap, 'top');
    }, false);
  }