%global debug_package %{nil}
%global _name QRandr

Name:		qrandr
Version:	2008.05.23
Release:	1
Summary:	Graphical screens configurator for Linux
License:	open source
Source0:	https://is.muni.cz/th/lmtbt/%{_name}.zip
Source1:	https://is.muni.cz/th/lmtbt/annotation_english.txt
Source2:        %{name}.desktop
Source3:        %{name}.png
Group:		User Interface/X
URL:            https://is.muni.cz/th/lmtbt/
BuildRequires:	gcc-c++, qt4-devel

%description
The QRandr utility for configuring screens on Linux.

%prep
%setup -q -n %{_name}
cp %{SOURCE1} .

%build
cd src
qmake-qt4 -o Makefile QRandr.pro
sed -i -e 's|-lX11|-lX11 -lXrandr|' -e 's|/usr/lib/|%{_libdir}/|g' Makefile
make QRandr

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 src/%{_name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc annotation_english.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 08 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 2008.05.23
- Rebuild for Fedora
