%define oname ManPageEditor

Name:                   manpageeditor
Version:                0.1.1
Release:                3.1
Summary:                Manual pages editor
License:                GPLv3
Group:                  Books/Howtos
URL:                    https://keithhedger.hostingsiteforfree.com/
Source0:                https://keithhedger.hostingsiteforfree.com/zips/manpageeditor/%{oname}-%{version}.tar.gz
BuildRequires:          desktop-file-utils
BuildRequires:          xdg-utils
BuildRequires:          pkgconfig(gtksourceview-2.0)
BuildRequires:      aspell-devel

%description
Create,edit,import,preview man-pages.

%prep
%setup -q -n %{oname}-%{version}
cp -r ManPageEditor/resources/docs/gpl-3.0.txt gpl-3.0.txt

%build
export CXXFLAGS=${CXXFLAGS/-Werror=format-security/}
./configure --prefix=/usr --enable-aspell
sed -i "s|update-mime-database /usr/share/mime||" Makefile
sed -i "/gtk-update-icon-cache/d" Makefile %{oname}/app/Makefile
sed -i "s|xdg-mime install ManPageEditor/resources/documenticons/maneditdoc-mime.xml||" Makefile
sed -i "s|-Wall|-Wall -fPIC|" Makefile %{oname}/app/Makefile

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/256x256/apps
%make_install
desktop-file-install $RPM_BUILD_ROOT%{_datadir}/applications/%{oname}.desktop
rm -fr $RPM_BUILD_ROOT%{_datadir}/%{oname}/docs

%files
%doc ChangeLog gpl-3.0.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/%{oname}/examples/*
%{_datadir}/%{oname}/help/*
%{_mandir}/man1/manpageeditor.1*
%{_datadir}/pixmaps/%{oname}.png
%{_datadir}/icons/hicolor/256x256/apps/%{oname}.png

%changelog
* Wed Jun 01 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.1
- Rebuilt for Fedora
* Wed Oct 23 2013 SymbianFlo <symbianflo@mandrivausers.ro> 0.0.13-1
+ Revision: 24b004a
- dropped mrb distsuffix, enable debug
