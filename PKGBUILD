# maintainer: skunga2kl@gmail.com

pkgname=what
pkgver=1.0.0
pkgrel=1
pkgdesc="A small Bash system information and smiley face script"
arch=('any')
url="https://github.com/luuggelis/what"
license=('MIT')
depends=('bash' 'coreutils' 'gawk' 'sed')

source=('what')
sha256sums=('SKIP')

package() {
    install -Dm755 "$srcdir/what" "$pkgdir/usr/bin/what"
}
