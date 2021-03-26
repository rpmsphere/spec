Name:               lockrun
Version:            1.0+4
Release:            3.1
Summary:            Run Cron Job with Overrun Protection
Source:             http://unixwiz.net/tools/lockrun.c
URL:                http://unixwiz.net/tools/lockrun.html
Group:              System/Base
License:            Public Domain
BuildRoot:          %{_tmppath}/build-%{name}-%{version}
BuildRequires:      gcc make glibc-devel

%description
When doing network monitoring, it's common to run a cron job every five minutes
(the standard interval) to roam around the network gathering data. Smaller
installations may have no trouble running within this limit, but in larger
networks or those where devices are often unreachable, running past the
five-minute mark could happen frequently.

The effect of running over depends on the nature of the monitoring application:
it could be of no consequence or it could be catastrophic. What's in common is
that running two jobs at once (the old one which ran over, plus the new one)
slows down the new one, increasing the risk that it will run long as well.

This is commonly a cascading failure which can take many polling sessions to
right itself, which may include lost data in the interim.

Our response has been to create this tool, lockrun, which serves as a
protective wrapper. Before launching the given command, it insures that another
instance of the same command is not already running. 

%prep
%setup -T -c
%__cp "%{SOURCE0}" .

%build
%__cc %{optflags} -Wall -o lockrun lockrun.c

%install
%__rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 lockrun "$RPM_BUILD_ROOT%{_bindir}/lockrun"

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%defattr(-,root,root)
%{_bindir}/lockrun

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0+4
- Rebuild for Fedora

* Sun Aug 29 2010 pascal.bleser@opensuse.org
- initial package (1.0+4)
