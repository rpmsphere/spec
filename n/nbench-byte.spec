%undefine _debugsource_packages

Name:          nbench-byte
Version:       2.2.3
Release:       6.1
Summary:       A port to Linux of BYTE Magazine's BYTEmark benchmark program
Group:         System/Hardware
URL:           https://www.math.utah.edu/~mayer/linux/bmark.html
Source0:       https://www.math.utah.edu/~mayer/linux/%{name}-%{version}.tar.gz
License:       GPL

%description
A Linux/Unix port of release 2 of BYTE Magazine's BYTEmark benchmark program
(previously known as BYTE's Native Mode Benchmarks). These are Native Mode
(a.k.a. Algorithm Level) tests; benchmarks designed to expose the capabilities
of a system's CPU, FPU, and memory system. Read all about it at BYTE's
benchmark page (https://www.byte.com/bmark/bmark.htm).

The benchmark program takes less than 10 minutes to run (on most machines) and
compares the system it is run on to two benchmark systems (a Dell Pentium 90
with 256 KB cache running MSDOS and an AMD K6/233 with 512 KB cache running Linux).

%prep
%setup -q
sed -i 's/-static//' Makefile

%build
make 

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cp nbench $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/nbench

%changelog
* Thu Nov 09 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.3
- Rebuilt for Fedora
* Sun May 20 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 2.2.2-1mamba
- update to 2.2.2
* Mon Jul 07 2003 Silvan Calarco <silvan.calarco@qinet.it> 2.2.1-1qilnx
- first build of nbench-byte
