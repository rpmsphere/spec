Name: gwc
Version: 0.22.04
Release: 1
Summary: GTK Wave Cleaner
License: GPLv2+
Group: Sound 
URL: http://gwc.sourceforge.net/
Source0: gtk-wave-cleaner-0.22-04.tar.gz
BuildRequires: alsa-lib-devel fftw-devel libgnomeui-devel libsndfile-devel

%description
Digital audio restoration of CD quality audio wavefiles. Dehiss, declick and
decrackle in a GUI environment.

%prep
%setup -qn gtk-wave-cleaner-0.22-04

%build
%configure --enable-alsa
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile
make CFLAGS+="`pkg-config --cflags gtk+-2.0` "

%install
%make_install

%files
%{_docdir}/gtk-wave-cleaner
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/icons/hicolor/*/apps/*
%exclude %{_datadir}/icons/hicolor/icon-theme.cache

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.22.04
- Rebuilt for Fedora
* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 0.21.17-alt1
- %%ver_major.%%ver_minor
* Sun Jun 19 2011 Victor Forsiuk <force@altlinux.org> 0.21.16-alt1
- 0.21-16.
* Fri Oct 01 2010 Victor Forsiuk <force@altlinux.org> 0.21.11-alt1
- 0.21-11.
* Tue Mar 24 2009 Victor Forsyuk <force@altlinux.org> 0.21.10-alt1
- 0.21-10.
* Sat Jan 10 2009 Victor Forsyuk <force@altlinux.org> 0.21.08-alt3
- Remove obsolete install time scripts.
* Wed Jul 04 2007 Victor Forsyuk <force@altlinux.org> 0.21.08-alt2
- Update build requirements (libSM-devel now have to be listed explicitly).
* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 0.21.08-alt1
- 0.21-08.
* Fri Jan 12 2007 Victor Forsyuk <force@altlinux.org> 0.21.07-alt1
- Initial build.
