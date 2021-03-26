Summary:	Simple animated GIF screen recorder
Name:		peek
Version:	1.3.1
Release:	3.1
License:	GPLv3+
Group:		Video
URL:		https://github.com/phw/peek
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	gettext-devel
BuildRequires:	vala
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:  pkgconfig(keybinder-3.0)

%description
Simple animated GIF screen recorder with an easy to use interface.

%prep
%setup -q

%build
%cmake
%make_build

%install
%make_install
%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/com.uploadedlobster.peek.desktop
%{_datadir}/dbus-1/services/com.uploadedlobster.peek.service
%{_datadir}/metainfo/com.uploadedlobster.peek.appdata.xml
%{_datadir}/glib-2.0/schemas/com.uploadedlobster.peek.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.uploadedlobster.peek.png

%changelog
* Wed Sep 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuild for Fedora
* Sun Mar 26 2017 tremod <negry.m@yandex.ru> 1.0.1-1
- (2271b3e) Update to 1.0.1
