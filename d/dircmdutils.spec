%undefine _debugsource_packages

Summary: Directory utilities
Name: dircmdutils
Version: 5.0
Release: 1
License: GPLv2
URL: https://www.tzclock.org
Group: Applications/Productivity
Source: https://www.tzclock.org/releases/%{name}-%{version}.tar.bz2
BuildRequires: ncurses-devel readline-devel libselinux-devel json-glib-devel libxml2-devel libacl-devel gcc
BuildRequires: libdircmd libdircmd-devel

%description
dirutils consists of a general purpose directory library and a number
of utilities that make use of that library.
 
%prep
%setup -q

%build
%configure 
make CDEBUGFLAGS="$RPM_OPT_FLAGS" CXXDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
install -s -m 755 addComment $RPM_BUILD_ROOT%{_bindir}/addComment
install -s -m 755 casedir $RPM_BUILD_ROOT%{_bindir}/casedir
install -s -m 755 casefile $RPM_BUILD_ROOT%{_bindir}/casefile
install -s -m 755 hexDump $RPM_BUILD_ROOT%{_bindir}/hexDump
install -s -m 755 jsonParse $RPM_BUILD_ROOT%{_bindir}/jsonParse
install -s -m 755 ldir $RPM_BUILD_ROOT%{_bindir}/ldir
install -s -m 755 lineDraw $RPM_BUILD_ROOT%{_bindir}/lineDraw
install -s -m 755 lineNum $RPM_BUILD_ROOT%{_bindir}/lineNum
install -s -m 755 lines $RPM_BUILD_ROOT%{_bindir}/lines
install -s -m 755 listFunc $RPM_BUILD_ROOT%{_bindir}/listFunc
install -s -m 755 pfile $RPM_BUILD_ROOT%{_bindir}/pfile
install -s -m 755 mkTable $RPM_BUILD_ROOT%{_bindir}/mkTable
install -s -m 755 modcr $RPM_BUILD_ROOT%{_bindir}/modcr
install -s -m 755 rmCppCmt $RPM_BUILD_ROOT%{_bindir}/rmCppCmt
install -s -m 755 tabSpace $RPM_BUILD_ROOT%{_bindir}/tabSpace
install -s -m 755 xmlParse $RPM_BUILD_ROOT%{_bindir}/xmlParse
install -m 644 ldirrc $RPM_BUILD_ROOT%{_sysconfdir}/ldirrc

%files
%{_bindir}/addComment
%{_bindir}/casedir
%{_bindir}/casefile
%{_bindir}/hexDump
%{_bindir}/jsonParse
%{_bindir}/ldir
%{_bindir}/lineDraw
%{_bindir}/lineNum
%{_bindir}/lines
%{_bindir}/listFunc
%{_bindir}/pfile
%{_bindir}/mkTable
%{_bindir}/modcr
%{_bindir}/rmCppCmt
%{_bindir}/tabSpace
%{_bindir}/xmlParse
%config(noreplace) %{_sysconfdir}/ldirrc

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 5.0
- Rebuilt for Fedora
* Wed Jan 31 2018 Chris Knight <chris@theknight.co.uk> 4.0.16-1
- Combined addrc and rmcr into one moderc.
* Wed Sep 26 2007 Chris Knight <chris@theknight.co.uk> 4.0.5-1
- Fixes to the build and distribution system.
