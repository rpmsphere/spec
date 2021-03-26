
Name:		lxp-icewm
Version:	1.2.30
Release:    	1.ossii
Summary:	Fast and small X11 window manager
Group:		User Interface/Desktops
License:	LGPL
URL:		http://lxp.sourceforge.net
Packager:   	Manuel Carrasco (manuel_carrasco@users.sourceforge.net)
Source:		http://lxp.sourceforge.net/lxp/%{name}-%{version}.tar.gz
Source1:	icewm-%{version}.zh_TW.po
Provides:	icewm

%define pkgdata %{_datadir}/%{name}

%description
A lightweight window manager for the X Window System. 
Optimized for feel, speed and looks identical to WinXP and others.
Features multiple workspaces, opaque move/resize, task bar, window list,
clock, mailbox, CPU, Network, APM, mixer status.

%if %{?_with_menus_gnome2:1}%{!?_with_menus_gnome2:0}

%package menu-gnome2
Group:		    %{group}
Summary:        GNOME menu support for lxp-icewm (using gnome 2.x).
Requires:       lxp-icewm > 1.2.2
Requires:       libgnome > 2.0.0
Requires:       gnome-vfs2 > 2.0.0

%description menu-gnome2
GNOME 1.0 menu support for lxp-icewm (using gnome 2.x).

%endif

%prep

%setup -q
%{__cp} -f %{SOURCE1} po/zh_TW.po

%build
  CXXFLAGS="$RPM_OPT_FLAGS" ./configure \
     --prefix=%{_prefix} \
     --exec-prefix=%{_exec_prefix} \
     --datadir=%{_datadir} \
     --sysconfdir=%{_sysconfdir} \
     --with-docdir=%{_docdir} \
     --enable-lookxp --enable-menu-leftpixmap --enable-taskbutton-over \
     --enable-gradients --enable-antialiasing --enable-xfreetype --enable-i18n \
     %{?_with_menus_gnome2:--enable-menus-gnome2} \
     %{?_with_debug:--enable-debug}
  make

%install
  make DESTDIR=$RPM_BUILD_ROOT install
  mkdir -p $RPM_BUILD_ROOT/etc/lxp-icewm

%clean
  test -n "$RPM_BUILD_ROOT" -a "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT

%files
%doc README COPYING AUTHORS CHANGES BUGS doc/*.html doc/icewm.sgml
%doc icewm.lsm

%config %{pkgdata}/keys
%config %{pkgdata}/menu
%config %{pkgdata}/preferences
%config %{pkgdata}/toolbar
%config %{pkgdata}/winoptions

%dir /etc/lxp-icewm

%dir %{pkgdata}/icons
%dir %{pkgdata}/ledclock
%dir %{pkgdata}/mailbox
%dir %{pkgdata}/mixer
%dir %{pkgdata}/taskbar
%dir %{pkgdata}/themes

%{_bindir}/lxp-icehelp
%{_bindir}/lxp-icesh
%{_bindir}/lxp-icewm
%{_bindir}/lxp-icewm-session
%{_bindir}/lxp-icewmbg
%{_bindir}/lxp-icewmhint
%{_bindir}/lxp-icewmtray

%{pkgdata}/icons/*
%{pkgdata}/ledclock/*
%{pkgdata}/mailbox/*
%{pkgdata}/mixer/*
%{pkgdata}/taskbar/*
%{pkgdata}/themes/*

%if %{?_with_menus_gnome2:1}%{!?_with_menus_gnome2:0}

%files menu-gnome2
%{_bindir}/lxp-icewm-menu-gnome2

%endif

%dir %{_datadir}/locale
%{_datadir}/locale/*

# %files themes
#%dir %{pkgdata}/themes/nice
#%{pkgdata}/themes/nice/*
#%dir %{pkgdata}/themes/nice2
#%{pkgdata}/themes/nice2/*
#%dir %{pkgdata}/themes/gtk2
#%{pkgdata}/themes/gtk2/*
#%dir %{pkgdata}/themes/warp3
#%{pkgdata}/themes/warp3/*
#%dir %{pkgdata}/themes/warp4
#%{pkgdata}/themes/warp4/*
#%dir %{pkgdata}/themes/motif
#%{pkgdata}/themes/motif/*
#%dir %{pkgdata}/themes/win95
#%{pkgdata}/themes/win95/*
#%dir %{pkgdata}/themes/metal2
#%{pkgdata}/themes/metal2/*
#%dir %{pkgdata}/themes/Infadel2
#%{pkgdata}/themes/Infadel2/*
#%dir %{pkgdata}/themes/yellowmotif
#%{pkgdata}/themes/yellowmotif/*
# %dir %{pkgdata}/themes/LookXP-WXP-Plain
# %{pkgdata}/themes/LookXP-WXP-Plain/*
# %dir %{pkgdata}/themes/LookXP-WXPBlue
# %{pkgdata}/themes/LookXP-WXPBlue/*
# %dir %{pkgdata}/themes/LookXP-WXPOlive
# %{pkgdata}/themes/LookXP-WXPOlive/*
# %dir %{pkgdata}/themes/LookXP-WXPSilver
# %{pkgdata}/themes/LookXP-WXPSilver/*
# %dir %{pkgdata}/themes/LookXP-Vista
# %{pkgdata}/themes/LookXP-Vista/*
# %dir %{pkgdata}/themes/LookXP-Human-Plain
# %{pkgdata}/themes/LookXP-Vista-Human/*
# %dir %{pkgdata}/themes/LookXP-Vista-Plain
# %{pkgdata}/themes/LookXP-Vista-Plain/*
# # # # # 

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Mar 19 2007 Wei-Lun Chao <bluebat@member.fsf.org> 1.2.30-1.ossii
- Update zh_TW locale
- Rebuild for 1.2.30
