Summary: Open Font Tools
Name: openfonttools
Version: 1.0.2
Release: 1
License: GPL
Group: System Environment/Utilities
Source: %{name}-%{version}.tar.gz
Requires: freetype, gd, fontforge, qt4
BuildRequires: freetype-devel, gd-devel, qt4-devel

%description
Collection of tools to manipulate TrueType Fonts.

%prep
%setup -q
rm -rf CVS */CVS
sed -i '1i #include <stdint.h>' qtui/cnspkgui.h

%build
%configure
make

cd qtui
qmake-qt4
sed -i 's|-Wall|-Wall -fpermissive|' Makefile
make

%install
rm -rf %{buildroot}
%makeinstall

rm -f %{buildroot}%{_bindir}/cnspkgen %{buildroot}%{_bindir}/unlink
install -D -m755 qtui/cnspkgui %{buildroot}%{_bindir}/cnspkgui
install -D -m755 win/makeudc.ffs %{buildroot}%{_bindir}/makeudc.ffs
mkdir -p %{buildroot}%{_datadir}/cnsfonttools/CNSFonts
cp win/*.TBL win/*.EUF win/*.TTF win/*.cin %{buildroot}%{_datadir}/cnsfonttools/CNSFonts

%clean
rm -rf %{buildroot}

%files
%doc COPYING AUTHORS INSTALL ChangeLog
%{_bindir}/*
%{_datadir}/cnsfonttools/CNSFonts

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2
- Rebuilt for Fedora
* Thu Aug 21 2008 Wei-Lun Chao <bluebat@member.fsf.org> 1.0.2-1.ossii
- Add CNSFonts files
* Thu Nov 15 2007 Wei-Lun Chao <bluebat@member.fsf.org> 1.0.1-2.ossii
- Rebuild for M6(CentOS5)
* Mon Jan 15 2007 Wei-Lun Chao <bluebat@member.fsf.org> 1.0.1-1.ossii
- Update to 1.0.1
* Mon Nov 20 2006 Wei-Lun Chao <bluebat@member.fsf.org> 1.0.0-1.ossii
- Initial package.
