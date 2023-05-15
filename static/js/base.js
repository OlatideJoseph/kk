function scrollNav(){
	let nav=document.getElementsByTagName('nav')[0];
	this.scrollY >= 50? nav.classList.add('nav-extended'):
	nav.classList.remove('nav-extended');
}
window.addEventListener('scroll',scrollNav);