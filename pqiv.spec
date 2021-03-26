%global _altdir /etc/alternatives

Name: pqiv
Version: 2.6
Release: 7.1
Summary: Minimalist Image Viewer
License: GPL3+
Group: Graphics
URL: https://github.com/phillipberndt/pqiv
Source: https://github.com/phillipberndt/pqiv/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: gtk2-devel gtk3-devel gdk-pixbuf2-devel glib2-devel cairo-devel
#BuildRequires: ffmpeg-devel
BuildRequires: poppler-devel poppler-glib-devel
BuildRequires: libspectre-devel
BuildRequires: ImageMagick-devel

%description
Originally, PQIV was written as a drop-in replacement for QIV.
This is common package, install either gtk2, gtk3 subpackages (or both).

%package gtk2
Summary: %name build with gtk2
Group: Graphics
Requires: %name = %version
%description gtk2
%name build with gtk2

%package gtk3
Summary: %name build with gtk3
Group: Graphics
Requires: %name = %version
%description gtk3
%name build with gtk3

%package gdkpixbuf
Summary: gdkpixbuf backend for %name
Group: Graphics
Requires: %name = %version
%description gdkpixbuf
Backend for %name

#%package libav
#Summary: libav backend for %name
#Group: Graphics
#Requires: %name = %version
#%description libav
#Backend for %name

%package poppler
Summary: poppler backend for %name
Group: Graphics
Requires: %name = %version
%description poppler
Backend for %name

%package spectre
Summary: spectre backend for %name
Group: Graphics
Requires: %name = %version
%description spectre
Backend for %name

%package wand
Summary: wand backend for %name
Group: Graphics
Requires: %name = %version
%description wand
Backend for %name

%prep
%setup -q
%ifarch x86_64 aarch64
sed -i 's|lib/%name|lib64/%name|' GNUmakefile
%endif

%build
for ver in 3 2;do
./configure \
--gtk-version=$ver \
--prefix=%_prefix \
--destdir=%buildroot \
--backends-build=shared \
--backends=gdkpixbuf,poppler,spectre,wand
#--backends=gdkpixbuf,libav,poppler,spectre,wand

%make_build
mv %name %{name}-gtk$ver
done
mv %{name}-gtk2 %name

%install
%make_install
mv %buildroot%_bindir/%name %buildroot%_bindir/%{name}-gtk2
install -p -m 755 %{name}-gtk3 %buildroot%_bindir/%{name}-gtk3

# Make alternatives:
mkdir -p %buildroot%_altdir
cat <<'_EOF'_ > %buildroot%_altdir/%name-gtk2
%_bindir/%name	%_bindir/%{name}-gtk2	10
_EOF_

cat <<'_EOF'_ > %buildroot%_altdir/%name-gtk3
%_bindir/%name	%_bindir/%{name}-gtk3	20
_EOF_

%files
%_mandir/man1/%name.1.*
%dir %_libdir/%name
%doc README.markdown

%files gtk2
%_altdir/%name-gtk2
%_bindir/%{name}-gtk2

%files gtk3
%_altdir/%name-gtk3
%_bindir/%{name}-gtk3

%files gdkpixbuf
%_libdir/%name/%name-backend-gdkpixbuf.so

#%files libav
#%_libdir/%name/%name-backend-libav.so

%files poppler
%_libdir/%name/%name-backend-poppler.so

%files spectre
%_libdir/%name/%name-backend-spectre.so

%files wand
%_libdir/%name/%name-backend-wand.so

%changelog
* Wed Nov 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuild for Fedora
* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt3
- Subpackages for gtk2/gtk3
* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt2
- Build backends: libav, poppler, spectre, wand
- Split to subpackages (one for backend)
* Sun Dec  6 2015 Terechkov Evgenii <evg@altlinux.org> 2.4.1-alt1
- Initial build for ALT Linux Sisyphus
- 2.4-40-gae7d440
