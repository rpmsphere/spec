Name:           deepin-terminal
Version:        1.1.7
Release:        6.1
Summary:        Terminal for Linux Deepin
License:        GPL3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{name}-%{version}.tar.gz
BuildArch:	    noarch
BuildRequires: 	deepin-gettext-tools
Requires: 	    python2, expect, deepin-utils, deepin-ui, hicolor-icon-theme, xdotool, deepin-gsettings, vte

%description
This is default terminal emulation application for Linux Deepin.
Deepin terminal base on python-vte and with many patches for advanced features,
such as, searching, opacity adjusting in real-time etc.

%prep
%setup -q

%build
deepin-generate-mo tools/locale_config.ini

%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=%{_prefix}
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/deepin-terminal
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/dman/%{name}
%{_datadir}/icons/hicolor/*
%doc README.md LICENSE

%changelog
* Thu Sep 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.7
- Rebuild for Fedora
* Mon Sep 28 2015 Derek Dai
- Initial package
