Name:				daemonizer
Version:			0.9.2
Release:			2.1
Summary:			Starts a Process while detaching it from the Terminal
# https://trac.id.ethz.ch/projects/daemonizer/downloads/10
Source:			daemonizer-%{version}.tar.bz2
URL:				https://trac.id.ethz.ch/projects/daemonizer/
Group:			System/Daemons
License:			The Apache License 2.0
BuildRoot:		%{_tmppath}/build-%{name}-%{version}
BuildRequires:	gcc make glibc-devel
BuildRequires:	autoconf automake libtool

%description
daemonizer is a tool that starts a process while detaching it from the
terminal. It makes the given process an orphan, closes all files descriptors,
and reopens standard input and output to a log file. This allows you to run
and program as a daemon.

Authors:
--------
    John Kelly
    Matteo Corti <matteo.corti@gmail.com>

%prep
%setup -q

%build
%configure
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%doc COPYRIGHT LICENSE NEWS TODO
%{_bindir}/daemonizer
%doc %{_mandir}/man1/daemonizer.1*

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuilt for Fedora

* Sun Apr 20 2008 Pascal Bleser <guru@unixtech.be> 0.9.2
- new package
