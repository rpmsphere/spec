%undefine _debugsource_packages

Name:           ghunter
BuildRequires:  libpng-devel
BuildRequires:  cmake gcc-c++ pkgconfig gtk2-devel libglade2-devel
Version:        0.0.5
Release:        23.1
License:        GPL v2 or later
Source:         ghunter_0.0.5.tar.gz
Patch0:         ghunter.desktop.diff
Group:          Productivity/Graphics/Viewers
Summary:        Picture watching program for comic books
URL:            https://ficl.sourceforge.net

%description
A set of picture-watching program intended to read comic books.

%prep
%setup -q
%patch0

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%buildroot install
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
mv $RPM_BUILD_ROOT/usr/share/ghunter/ghunter-icon.png $RPM_BUILD_ROOT/usr/share/pixmaps/ghunter.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README ChangeLog
%dir %{_datadir}/ghunter
%{_bindir}/ghunter
%{_datadir}/locale/zh_TW/LC_MESSAGES/ghunter.mo
%{_datadir}/applications/ghunter.desktop
%{_datadir}/ghunter/ghunter.glade
%{_datadir}/pixmaps/ghunter.png

%changelog
* Thu Mar 03 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.5
- Rebuilt for Fedora
* Sun Nov 23 2008 swyear@yahoo.com.tw
- packaged ghunter version 0.0.4 using the buildservice spec file wizard
