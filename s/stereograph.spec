%global debug_package %{nil}

Name: stereograph
Version: 0.33b
Release: 5.1
Summary: Stereogram generator
License: GPL
Group: Graphics
URL: http://stereograph.sourceforge.net/
Source: %name-%version.tar.bz2
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel

%description
Stereograph is a stereogram generator. In detail it is a single image
stereogram (SIS) generator. That is a program that produces
two-dimensional images that seem to be three-dimensional (surely you
know the famous works of "The Magic Eye", Stereograph produces the
same output). You do _not_ need any pair of colored spectacles to
regard them - everyone can learn it.

%prep
%setup -q
sed -i 's|png_ptr->jmpbuf|png_jmpbuf(png_ptr)|' gfxio.c
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile

%build
make

%install
install -pD -m 755 %name %buildroot%_bindir/%name
install -pD -m 644 %name\.1 %buildroot%_mandir/man1/%name\.1

%files
%_bindir/%name
%_mandir/man1/*
%doc README ChangeLog AUTHORS COPYING

%changelog
* Wed Jul 08 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.33b
- Rebuild for Fedora
* Mon Feb 11 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt2
- Fix to build against libpng-1.5.x.
* Sat Feb 09 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt1
- Build for Sisyphus.
* Fri Feb 08 2013 Dmitry Derjavin <dd@altlinux.org> 0.30a-alt0.M60P.1
- Initial build for ALT Linux P6.
