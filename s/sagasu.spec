Summary: Tool to find strings in a set of files
Name: sagasu
Version: 2.0.12
Release: 4.4
License: GPL
Group: Applications/Text
URL: http://sarrazip.com/dev/sagasu.html
Source: http://www3.sympatico.ca/sarrazip/dev/sagasu-%{version}.tar.gz
BuildRequires: libgnomeui-devel
BuildRequires: gcc-c++
BuildRequires: w3m udisks2
Requires: libgnomeui

%description
The user specifies the search directory and the set of files
to be searched.  Double-clicking on a search result launches a
user command that can for example load the file in an editor
at the appropriate line.  The search can optionally ignore
CVS directories.

%prep
%setup -q
sed -i 's|<glib/.*>|<glib.h>|' src/util.h
sed -i '1i #include <cstring>\n#include <cstdlib>' src/util.h

%build
%configure \
	--disable-dependency-tracking
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%make_install
%find_lang %{name}

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%doc %{_mandir}/man?/*
%doc %{_datadir}/gnome/help/sagasu
%{_bindir}/*
%{_datadir}/sagasu
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*
%exclude %{_docdir}

%changelog
* Tue Feb 24 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.12
- Rebuild for Fedora
* Wed Jan 25 2006 Dries Verachtert <dries@ulyssis.org> - 2.0.8-1 - 4004/dries
- Updated to release 2.0.8.
* Sat Jun 12 2004 Dag Wieers <dag@wieers.com> - 2.0.6-1
- Updated to release 2.0.6.
* Sat Oct 25 2003 Dag Wieers <dag@wieers.com> - 2.0.5-0
- Updated to release 2.0.5.
* Wed Oct 22 2003 Dag Wieers <dag@wieers.com> - 2.0.4-0
- Updated to release 2.0.4.
* Thu Jul 31 2003 Dag Wieers <dag@wieers.com> - 2.0.3-0
- Updated to release 2.0.3.
* Sun Jun 01 2003 Dag Wieers <dag@wieers.com> - 2.0.2-0
- Updated to release 2.0.2.
* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 2.0.1-0
- Updated to release 2.0.1.
* Sat May 17 2003 Dag Wieers <dag@wieers.com> - 1.0.6-0
- Initial package. (using DAR)
