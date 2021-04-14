%undefine _debugsource_packages

Name:			grepcidr
Version:		1.3
Release:		5.1
License:		GPLv2
Group:			Productivity/Networking/Other
Summary:		Filter IP addresses matching IPv4 CIDR specification
URL:			http://www.pc-tools.net/unix/grepcidr/
Source:			%{name}-%{version}.tar.bz2

%description
grepcidr can be used as a stream filter when you need to compare a list of IP
addresses against one or more Classless Inter-Domain Routing (CIDR) mask
specifications. Think of grepcidr as a CIDR-aware grep; instead of using
'grep 1.2.3.4' you can use 'grepcidr -e 1.2.3.4/30', for example. Multiple
specifications, of arbitrary mask lengths, can be specified both on the
command line or loaded from a file.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/*
%doc COPYING ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Aug 01 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Sun Apr 24 2005 Jem Berkes <jb@users.pc9.org>
- Version 1.3
- ===========
- Much faster than past versions due to binary search of patterns
- Decreased memory usage
- Applied search improvements suggested by Dick Wesseling <ftu@fi.uu.nl>
- Now supports IP ranges as well as CIDR format
- Improved usage to be more grep-like (e.g. filename on command line)
- Now uses grep-like exit code (0=ok, 1=no match, 2=error)
* Fri Apr 23 2004 Jem Berkes <jb@users.pc9.org>
- Version 1.2
- ===========
- Improved algorithm for faster processing with large number of patterns
- (approx. 50 times as fast on test set, with specs from diverse regions)
#*  2004 Jem Berkes <jb@users.pc9.org>
#- Version 1.1
#- ===========
#- New algorithm has increased speed by about 2.4 times!
#- Added -c (count) option, like grep
#- Reduced memory usage in case loading large files (-f)
#- Added simple Makefile
* Sat Feb 14 2004 Jem Berkes <jb@users.pc9.org>
- Version 1.0
- ===========
- First public release
