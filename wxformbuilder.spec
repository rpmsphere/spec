%global debug_package %{nil}
%global oname wxFormBuilder

Summary:	An open-source, cross-platform RAD tool for wxWidgets
Name:		wxformbuilder
Version:	3.8.1git
Release:	4.1
License:	GPLv2
Group:		Development/Tools 
URL:		https://github.com/wxFormBuilder/wxFormBuilder
Source0:	%{oname}-master.zip
BuildRequires:	gcc-c++
BuildRequires:	ImageMagick
BuildRequires:	wxGTK3-devel

%description
wxFormBuilder is an open-source, cross-platform RAD tool for wxWidgets. 
It aims to be an application that as well as enabling visual development 
and generating the corresponding code for C++, Python, PHP, Lua and XRC,
allows the inclusion of non-graphical components, as well as providing
facilities for extending the set of widgets easily via plugins.

%prep
%setup -q -n %{oname}-master

%build
sh create_build_files4.sh
cd build/3.0/gmake
make config=release all

%install
install -d -m 0755 %buildroot%{_bindir}
install -d -m 0755 %buildroot%{_libdir}/%{name}
install -d -m 0755 %buildroot%{_datadir}/%{name}
install -d -m 0755 %buildroot%{_datadir}/applications
install -d -m 0755 %buildroot%{_datadir}/icons

cd output
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mv bin/* %{buildroot}%{_bindir}
mv lib/* %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mv plugins resources xml %{buildroot}%{_datadir}/%{name}

# Icons
for s in 128 96 48 32 22 16 ; do
	mkdir -p %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps
	convert %{buildroot}%{_datadir}/%{name}/resources/icons/logo.png -resize ${s}x${s} %{buildroot}%{_datadir}/icons/hicolor/${s}x${s}/apps/%{name}.png
done
	
# menu-entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{oname}
Comment=GUI designer for wxWidgets
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Development;IDE;GUIDesigner;
EOF

%clean
rm -rf %{buildroot}

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.*

%changelog
* Wed Oct 03 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.8.1git
- Rebuild for Fedora
* Mon Dec 14 2015 Oleg Kozlov <xxblx.oleg@yandex.com> 3.5.0beta-1.mga5
- built for mageia 5
* Sun May 10 2015 Oleg Kozlov <xxblx.oleg@yandex.com> 3.5.0beta-3.mga4
- Requires and install fixes
* Sat Jun 07 2014 Oleg xxblx 3.5.0beta
+ wxFormBuilder 3.5.0-beta 
- license fix
* Fri Mar 21 2014 Oleg xxblx 3.4.2beta
+ wxFormBuilder 3.4.2-beta 
- Build for Mageia 4 (wxWidgets 2.9.5)
