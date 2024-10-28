Summary: Shostakovich is a happy smiley man
Name: xshostakovich
Version: 1.7
Release: 13.1
Source: https://www.lcdf.org/~eddietwo/xshostakovich/xshostakovich-1.7.tar.gz
URL: https://www.lcdf.org/~eddietwo/xshostakovich/
Group: X11/Amusements
BuildRequires: libX11-devel
License: GPL

%description
Xshostakovich displays a virtual Dmitri
Dmitrievich Shostakovich for your own personal
use!! All the boyish charm with none of the moral
fiber or musical genius!!

%prep
%setup -q
sed -i 's| = "#497955"||' xshostakovich.hh
sed -i '49i const char * const Shostakovich::BackgroundColor = "#497955";' xshostakovich.cc

%build
export CFLAGS="$RPM_OPT_FLAGS"
./configure --prefix=$RPM_BUILD_ROOT/usr
sed -i 's|-Wall|-Wall -Wno-narrowing -std=c++98|' Makefile
make

%install
make install
mkdir -p $RPM_BUILD_ROOT/usr/share
mv $RPM_BUILD_ROOT/usr/man $RPM_BUILD_ROOT/usr/share/man

%files
%doc NEWS README
%{_bindir}/xshostakovich
%{_mandir}/man6/xshostakovich.6.*

%changelog
* Tue May 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Thu Feb 10 2000 Eddie Kohler <eddietwo@lcs.mit.edu>
- Initial package
