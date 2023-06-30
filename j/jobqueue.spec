Name:				jobqueue
Version:			0.04
Release:			3.1
Summary:			Execute Jobs in Parallel
Source:			https://zakalwe.fi/~shd/foss/jobqueue/jobqueue-%{version}.tar.bz2
Patch1:			jobqueue-optflags.patch
URL:				https://zakalwe.fi/~shd/foss/jobqueue/
Group:			Productivity/Clustering/Computing
License:			Public Domain
BuildRequires:	gcc glibc-devel

%description
jobqueue is a program for executing jobs in parallel to complete all jobs as
fast as possible. It can be used to distribute a set of jobs to a specific
number of processors and/or machines. New jobs are started as older jobs
finish.

Authors:
--------
    Heikki Orsila <heikki.orsila@iki.fi>

%prep
%setup -q
%patch1

%build
./configure --prefix="%{_prefix}" --package-prefix="$RPM_BUILD_ROOT"
%__make %{?jobs:-j%{jobs}} OPTFLAGS="%{optflags}"

%install
%__rm -rf "$RPM_BUILD_ROOT"
make DESTDIR=$RPM_BUILD_ROOT install

%clean
%__rm -rf "$RPM_BUILD_ROOT"

%files
%doc AUTHORS ChangeLog COPYING README.txt TO_DO
%{_bindir}/jobqueue

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.04
- Rebuilt for Fedora

* Mon Aug 25 2008 Pascal Bleser <guru@unixtech.be> 0.04
- update to 0.04:
  * machine list (-m) can now be used to specify the maximum number of
    simultaneous jobs for each machine.

* Thu Apr  3 2008 Pascal Bleser <guru@unixtech.be> 0.03
- disabling make check, causes a deadlock

* Sun Mar 23 2008 Pascal Bleser <guru@unixtech.be> 0.03
- new upstream version

* Fri Jan 11 2008 Pascal Bleser <guru@unixtech.be> 0.02
- new upstream version

* Tue Dec 25 2007 Pascal Bleser <guru@unixtech.be> 0.01
- new package
