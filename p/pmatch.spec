Name:				pmatch
Version:			0.3.1
Release:			2.1
Summary:			Small and Fast Utility for Finding Duplicate Files
Source:			https://rubyforge.org/frs/download.php/31027/pmatch-%{version}.tar.bz2
URL:				https://pmatch.rubyforge.org/
Group:			Productivity/File utilities
License:			GNU General Public License version 3 (GPL v3)
Requires:		rubygem-log4r
BuildArch:		noarch

%description
Perfect Match (pmatch) is a small and fast commandline utility for finding
duplicate files.

Authors:
--------
    nexor@fnet.pl

%prep
%setup -q -c "%{name}-%{version}"

%build

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 pmatch "$RPM_BUILD_ROOT%{_bindir}/pmatch"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/pmatch

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.1
- Rebuilt for Fedora

* Sun Jan 20 2008 Pascal Bleser <guru@unixtech.be> 0.3.1
- new package
