%define         srcname        fvwm3
%define         cfgname        %{name}-config-mageia
%define         fvwmconfdir    %{_sysconfdir}/fvwm3
%define         docname        %{name}-doc

Name:           fvwm3
Version:        1.0.4
Release:        2
Summary:        FVWM version 3, the successor to fvwm2 
License:        GPLv2+
Group:          Graphical desktop/Other

URL:            https://www.fvwm.org/
Source0:        https://github.com/fvwmorg/fvwm/releases/download/%{version}/%{srcname}-%{version}.tar.gz

#block-logo
Source1:        fvwm3.png
#minimal system-wide config to be installed as system.fvwm2rc
Source2:        system-minimal.fvwm3rc
#minimal configuration file, called from the system-minimal.fvwm2rc
Source3:        fvwm3rc-minimal.mga

# to get an icon on the xterm button
Source6:        fvwm3_terminal.png

#enhanced config files for mageia default settings
Source7:        system-mageia.fvwm3rc
Source8:        fvwm3rc-extra.mga
Source9:        fvwm3.desktop

#Patch0:         fvwm3-1.0.0-format.patch

BuildRequires:  flex
BuildRequires:  sharutils
BuildRequires:  xsltproc
BuildRequires:  golang
BuildRequires:  pkgconfig(pkg-config)
BuildRequires:  pkgconfig(libbson-1.0)
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xt)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(xcursor)
BuildRequires:  pkgconfig(sm)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xi)
BuildRequires:  pkgconfig(xpm)
BuildRequires:  pkgconfig(imlib2)
BuildRequires:  readline-devel
BuildRequires:  rubygem-asciidoctor

#BuildRequires:  pkgconfig(tinfo)
#BuildRequires:  libstroke-devel
#BuildRequires:  pkgconfig(librsvg-2.0)
#BuildRequires:  pkgconfig(xinerama)



# for fvwm-menu-headlines
Requires:       desktop-common-data
# for fvwm-menu-xlock
Requires:       xlockmore
# for doing something
Requires:       xterm
# for iconification and wallpaper
Requires:       xwd
Requires:       imagemagick
Requires:       feh
# for mimeinfo
Requires:       perl-File-MimeInfo
# for compositing (enhancement only)
Recommends:       xcompmgr
Recommends:       transset-df
Conflicts:        fvwm2
Requires:         %{name}-doc
Requires(post):      update-alternatives
Requires(postun):    update-alternatives
Requires(posttrans): update-alternatives

%description
Fvwm3 is a multiple large virtual desktop window manager, originally
(a looooong time ago, 1993!) derived from twm. Shortly, it is the successor
to fvwm2. Fvwm3 is intended to have a small memory footprint but a
rich feature set, be extremely customizable and extendible, and have a
high degree of Motif mwm compatibility. Currently, your existing fvwm2
config will work with fvwm3.

%package -n %{cfgname}
Summary:        Mageia system-wide configuration for Fvwm3
Group:          Graphical desktop/Other
Requires:       fvwm3
#for button bar
Requires:       wmcalclock
Requires:       wmtop
%ifarch %{ix86} x86_64
Requires:       wmcpufreq
%endif
Requires:       wmforkplop
Requires:       wmhdplop
Requires:       wmbutton
Requires:       wmmoonclock
Requires:       wmsystemtray
# for the menu
Requires:       rxvt-unicode
Recommends:     terminology
# for fvwm-bug
Recommends:     sendmail-command

Requires(post):      update-alternatives
Requires(postun):    update-alternatives

%description -n %{cfgname}
%{summary}.

%package -n %{docname}
Summary:        Documentation files for Fvwm3
Group:          Graphical desktop/Other
Conflicts:      fvwm2-doc

%description -n %{docname}
%{summary}.

%prep
%setup -q -n %{srcname}-%{version}
%autopatch -p1
autoreconf -fi

%build
%configure \
    --enable-mandoc \
    --sysconfdir=%{fvwmconfdir} \
    --with-imagepath=%{_datadir}/pixmaps \
    --disable-golang

%make_build LOCALEDIR=%{_datadir}/locale localedir=%{_datadir}/locale
  
%install
%{make_install} LOCALEDIR=%{_datadir}/locale localedir=%{_datadir}/locale
install -D -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/fvwm3.png
install -D -m644 %{SOURCE2} %{buildroot}%{fvwmconfdir}/system-minimal.fvwm3rc
install -D -m644 %{SOURCE3} %{buildroot}%{fvwmconfdir}/fvwm3rc-minimal.mga
install -D -m644 %{SOURCE6} %{buildroot}%{_datadir}/pixmaps/fvwm3_terminal.png
install -D -m644 %{SOURCE7} %{buildroot}%{fvwmconfdir}/system-mageia.fvwm3rc
install -D -m644 %{SOURCE8} %{buildroot}%{fvwmconfdir}/fvwm3rc-extra.mga
install -D -m644 %{SOURCE9} %{buildroot}%{_datadir}/xsessions/fvwm3.desktop
%find_lang %{name} --all-name

%files -f %{name}.lang
%doc NEWS COPYING
%config(noreplace) %{fvwmconfdir}/fvwm3rc-minimal.mga
%config(noreplace) %{fvwmconfdir}/system-minimal.fvwm3rc
%{_bindir}/*
%{_libexecdir}/%{name}
%{_datadir}/xsessions/fvwm3.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/fvwm3.png
%{_mandir}/man1/fvwm3.1*

%post
#if the file has been edited, or so, it is a regular file
#and not a symlink. So we first rename it before calling
#update-alternatives to create the symlink.
if [ -f %{fvwmconfdir}/system.fvwm3rc -a ! -h %{fvwmconfdir}/system.fvwm3rc ]; then
    mv %{fvwmconfdir}/system.fvwm3rc %{fvwmconfdir}/system.fvwm3rc.rpmold
fi
update-alternatives --install %{fvwmconfdir}/system.fvwm3rc fvwm3-config \
                    %{fvwmconfdir}/system-minimal.fvwm3rc 10

%postun
#uninstall only
if [ $1 -eq 0 ]; then
   update-alternatives --remove fvwm3-config %{fvwmconfdir}/system-minimal.fvwm3rc
fi

%posttrans
#old releases had system.fvwm3rc as file packaged in, so our symlink
#will be removed if one upgrade from those.
if ! [ -h %{fvwmconfdir}/system.fvwm3rc ]; then
   update-alternatives --install %{fvwmconfdir}/system.fvwm3rc fvwm3-config \
                    %{fvwmconfdir}/system-minimal.fvwm3rc 10
fi

# (ovitters) In posttrans, $1 is always equal to 1, even in the upgrade case.
# So just run this always:
if [ -e %{_datadir}/xsessions/09Fvwm3.desktop ]; then
        rm -rf %{_datadir}/xsessions/09Fvwm3.desktop
fi
if [ -e %{_sysconfdir}/X11/dm/Sessions/09Fvwm3.desktop ]; then
        rm -rf %{_sysconfdir}/X11/dm/Sessions/09Fvwm3.desktop
fi

%files -n %{cfgname}
%config(noreplace) %{fvwmconfdir}/fvwm3rc-extra.mga
%config(noreplace) %{fvwmconfdir}/system-mageia.fvwm3rc
%{_datadir}/pixmaps/fvwm3_terminal.png

%post -n %{cfgname}
if [ -f %{fvwmconfdir}/system.fvwm3rc -a ! -h %{fvwmconfdir}/system.fvwm3rc ]; then
    mv %{fvwmconfdir}/system.fvwm3rc %{fvwmconfdir}/system.fvwm3rc.rpmold
fi
update-alternatives --install %{fvwmconfdir}/system.fvwm3rc fvwm3-config \
                    %{fvwmconfdir}/system-mageia.fvwm3rc 11

%postun -n %{cfgname}
if [ $1 -eq 0 ]; then
   update-alternatives --remove fvwm3-config %{fvwmconfdir}/system-mageia.fvwm3rc
fi

%files -n %{docname}
%{_mandir}/man1/Fvwm*
%{_mandir}/man1/fvwm-*
#{_mandir}/man1/xpmroot*

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.4
- Rebuilt for Fedora
* Thu Aug 26 2021 eatdirt <eatdirt> 1.0.4-2.mga9
+ Revision: 1742663
- Fix configuration files due to breakage induced by 1.0.4
* Thu Aug 26 2021 eatdirt <eatdirt> 1.0.4-1.mga9
+ Revision: 1742648
- Upgrade to version 1.0.4 and set conflicts with fvwm2
* Mon May 17 2021 eatdirt <eatdirt> 1.0.2-2.mga9
+ Revision: 1725199
- Fix self-conflict
* Tue Dec 22 2020 eatdirt <eatdirt> 1.0.2-1.mga8
+ Revision: 1662889
- Upgrade to version 1.0.2
* Sun Dec 13 2020 eatdirt <eatdirt> 1.0.1-1.mga8
+ Revision: 1656060
- Upgrade to 1.0.1
* Sat Sep 05 2020 eatdirt <eatdirt> 1.0.0-2.mga8
+ Revision: 1622471
- Build man
* Fri Sep 04 2020 eatdirt <eatdirt> 1.0.0-1.mga8
+ Revision: 1622233
- Using std configure macro
- imported package fvwm3
