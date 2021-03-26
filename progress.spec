Summary:			File I/O Progress Monitor Utility
Name:				progress
Version:			1.10
Release:			5.1
Source:			http://ftp.unixdev.net/pub/debian-udev/pool/main/p/progress/progress_%{version}.orig.tar.gz
Patch1:			http://ftp.unixdev.net/pub/debian-udev/pool/main/p/progress/progress_%{version}-2.diff.gz
Patch2:			progress-makefile.diff
Patch3:			progress-remove-asm_system-include.patch
URL:				http://progress.unixdev.net/
Group:			System/Benchmark
License:			BSD
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	make gcc glibc-devel

%description
The progress utility allows progress to be monitored of file I/O.
It includes support for gzip-compressed files, so "progress -z -f file.tar.gz
tar xf -" would show progress of extracting file.tar.gz.

It's a port of the original NetBSD progress utility to Linux and Solaris.

%prep
%setup -q -n progress
%patch1 -p1
%patch2
%patch3

%build
# it's not autoconf
%__chmod +x ./configure
./configure

%__make \
	%{?jobs:-j%{jobs}} \
	CC="%__cc" \
	CFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m 0755 progress "$RPM_BUILD_ROOT%{_bindir}/progress"
%__install -D -m 0755 progress.1 "$RPM_BUILD_ROOT%{_mandir}/man1/progress.1"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/progress
%doc %{_mandir}/man1/progress.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10
- Rebuild for Fedora

* Mon Oct 22 2007 Pascal Bleser <guru@unixtech.be> 1.10
- moved to openSUSE Build Service

* Thu Nov 23 2006 Pascal Bleser <guru@unixtech.be> 1.10-2
- pass -j
- rewrote spec file

* Wed Nov  9 2005 Pascal Bleser <guru@unixtech.be> 1.10-1
- new package
