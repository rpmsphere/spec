%global	_name Chicago95

Name:           chicago95
Version:        3.0.1
Release:        1
Summary:        A rendition of everyone's favorite 1995 Microsoft operating system for Linux
License:        MIT, GPLv3+
URL:            https://github.com/grassmunk/Chicago95
Source0:        https://github.com/grassmunk/Chicago95/archive/refs/tags/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  txt2man

%description
I was unhappy with the various XFCE/GTK2/GTK3 Windows 95 based themes and
decided to make one that was more consistent across the board for theming.

Included in this theme:
* New icons to complete the icon theme started with Classic95
* GTK2 and GTK3 themes
* Edited Redmond XFWM theme to more accurately reflect Windows 95
* Chicago95 Plus! A tool to preview and install Windows 95/98/ME/XP themes
* Plymouth theme created from scratch
* An MS-DOS inspired theme for oh-my-zsh
* Partial support for HiDPI monitors
* Partial icon theme for Libre Office 6+

%prep
%autosetup -n %{_name}-%{version}

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
install CREDITS README.md %{buildroot}%{_docdir}/chicago95

%files
%{_docdir}/chicago95
%{_bindir}/*
%{_datadir}/themes/%{_name}
%{_datadir}/icons/%{_name}*
%{_datadir}/sounds/%{_name}
%{_datadir}/xfce4/terminal/colorschemes/%{_name}.theme
%{_sysconfdir}/xdg/autostart/%{name}-startup.desktop
%{_libexecdir}/%{name}-theme-plus
%{_datadir}/%{name}-theme-plus
%{_datadir}/fonts/truetype/*
%{_datadir}/plymouth/themes/*
%{_datadir}/applications/PlusGUI.desktop
%{_datadir}/backgrounds/Chicago95
%{_mandir}/man1/*.1*
%{_datadir}/mime/packages/chicago95-plus-theme.xml
%{_datadir}/xfce4-panel-profiles/layouts/Chicago95_Panel_Preferences.tar.bz2
   
%changelog
* Sun Jan 15 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
