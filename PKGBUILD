# maintainer: skunga2kl@gmail.com

pkgname=what
pkgver=1.0.0
pkgrel=1
pkgdesc="A small Bash system information and smiley face script"
arch=('any')
url="https://github.com/luuggelis/what"
license=('MIT')
depends=('python')

source=('what.py')
sha256sums=('SKIP')

package() {
	install -Dm755 "$srcdir/what.py" "$pkgdir/usr/bin/what"
}
