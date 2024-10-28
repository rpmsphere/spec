Summary:        X11 Window Manager - Windows 95/98 alike
Name:           qvwm
Version:        1.1.12
Release:        24.1
License:        LGPL
Group:          Graphical desktop/Other
Source0:        ftp://ftp.qvwm.org/pub/qvwm/%{name}-%{version}.tar.bz2
Patch0:         %{name}-am15.patch.bz2
Patch1:         %{name}-man_MANS.patch.bz2
URL:            https://www.qvwm.org/
BuildRequires:  gcc-c++, automake
BuildRequires:  esound-devel >= 0.2.6
BuildRequires:  flex
BuildRequires:  imlib-devel >= 1.8.2
BuildRequires:  libXpm-devel

%description
Qvwm is a Windows 95/98/NT like window manager for X Window System. It
allows Windows 95/98/NT users to use X Window System without
hesitation and X Window System users to use Windows 95/98/NT without
hesitation.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1

%build
rm -f missing configure
aclocal
automake -a
autoconf
# -a -c -f
CXXFLAGS="$RPM_OPT_FLAGS -fno-exceptions -fno-rtti -Wno-narrowing"
%configure \
    --prefix=%{_prefix} \
        --sysconfdir=%{_sysconfdir}/X11 \
        --enable-rmtcmd \
        --enable-xsmp \
        --enable-ss

make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT                                    

mkdir -p $RPM_BUILD_ROOT%{_datadir}/xsessions
cat > $RPM_BUILD_ROOT%{_datadir}/xsessions/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=QvWM
Comment=A strong solution for a Windows 95/98 like environment
TryExec=%{name}
Exec=%{name}
Type=Xsession
EOF

mv -f $RPM_BUILD_ROOT/%{_mandir}/jp $RPM_BUILD_ROOT/%{_mandir}/ja

%files
%{_prefix}/bin/*
%{_prefix}/share/%{name}
%{_mandir}/man?/*
%{_mandir}/fr/man?/*
%{_mandir}/ja/man?/*
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Mon Jul 30 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.12
- Rebuilt for Fedora
* Fri Jun 30 2006 Olivier Thauvin <nanardon@zarb.org> 1.1.12-8plf
- add plf reason
- change prefix
* Sun Oct  9 2005 Stefan van der Eijk <stefan@zarb.org> 1.1.12-7plf
- BuildRequires
- Note: URL is no longer valid
* Mon Mar 28 2005 Olivier Thauvin <nanardon@zarb.org> 1.1.12-6plf
- rebuild && %%mkrel
* Fri Jul 25 2003 Michael Scherer <scherer.michael@free.fr> 1.1.12-5plf
- Fix unpackaged files, by moving japanese manpages
* Sun Nov 10 2002 Stefan van der Eijk <stefan@eijk.nu> 1.1.12-4plf
- BuildRequires
* Mon Sep 02 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.12-3plf
- => plf (win icones)
* Mon Sep 02 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.12-3mdk
- rebuild
* Sat Aug 03 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.12-2mdk
- add buildrequires flex (thx Han) 
* Mon Jun 24 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 1.1.12-1mdk
- mdk adaptation from pld
