%undefine _debugsource_packages

Name:		apwal
Version:	0.4.5
Release:	1
License:	GPL
Group:		User Interface/Desktops
Summary:	application launcher
Source0:	https://apwal.free.fr/download/%{name}-%{version}.tar.gz
Source1:	%{name}-editor.desktop
Source2:	%{name}-editor.sh
Source3:        https://apwal.free.fr/img/apwal-launcher-small.png
URL:		https://apwal.free.fr/
BuildRequires:	pkgconfig
BuildRequires:	gtk2-devel 
BuildRequires:	libxml2-devel

%description
Apwal is a simple application launcher for Linux together with
a powerful editor. Apwal is developed under the GPL Licence.
It is written in C and use the GTK+ toolkit for the graphical
interface and XML format to save the settings.

%prep 
%setup -q -n apwal

%build
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__install} -Dm 755 src/apwal %{buildroot}%{_bindir}/apwal
%{__install} -Dm 644 %{SOURCE1} %{buildroot}%{_datadir}/applications/apwal-editor.desktop
%{__install} -Dm 755 %{SOURCE2} %{buildroot}%{_bindir}/apwal-editor
%{__install} -Dm 644 %{SOURCE3} %{buildroot}%{_datadir}/pixmaps/apwal.png

%clean
%{__rm} -rf %{buildroot}

%files
%doc ABOUT Changelog README FAQ
%attr(755,root,root)  %{_bindir}/apwal*
%{_datadir}/applications/apwal-editor.desktop
%{_datadir}/pixmaps/apwal.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.5
- Rebuilt for Fedora
* Sun Oct 15 2006 Piotr Pacholak <obi.gts@gmail.com>
- SUSE 10.1
* Sun May 28 2006 Piotr Pacholak <obi.gts@gmail.com>
- Added "apwal-editor"
* Sun May 28 2006 Piotr Pacholak <obi.gts@gmail.com>
- initial release
