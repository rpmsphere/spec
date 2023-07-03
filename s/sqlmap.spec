# binaries are exploits, intended to be used on remote systems
%define _binaries_in_noarch_packages_terminate_build 0

# exclude binaries from dependencies computing
%global __requires_exclude_from ^%{_datadir}/%{name}/udf/.*$
%global __provides_exclude_from ^%{_datadir}/%{name}/udf/.*$

Name:           sqlmap
Version:        0.9
Release:        6.1
Summary:        Automatic SQL injection and database takeover tool
Group:          Security
License:        GPL
URL:            https://sqlmap.org/
Source0:        https://github.com/sqlmapproject/sqlmap/tarball/master/sqlmapproject-sqlmap-0.9-3451-g17742df.tar.gz
Patch0:         sqlmap-1.0-disable-svn-lookup.patch
BuildArch:      noarch

%description
sqlmap is an open source penetration testing tool that automates the process
of detecting and exploiting SQL injection flaws and taking over of database
servers. It comes with a powerful detection engine, many niche features for
the ultimate penetration tester and a broad range of switches lasting from
database fingerprinting, over data fetching from the database, to accessing
the underlying file system and executing commands on the operating system
via out-of-band connections.

%prep
%setup -q -n sqlmapproject-sqlmap-17742df
#patch0 -p 1
find . -name .svn | xargs rm -rf
# use a static revision, as we don't ship svn admin files
#perl -pi -e 's/\@snapshot\@/17742df/' lib/core/settings.py

%install
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 sqlmap.py %{buildroot}%{_datadir}/%{name}
cp -pr extra %{buildroot}%{_datadir}/%{name}
cp -pr lib %{buildroot}%{_datadir}/%{name}
cp -pr plugins %{buildroot}%{_datadir}/%{name}
cp -pr procs %{buildroot}%{_datadir}/%{name}
cp -pr shell %{buildroot}%{_datadir}/%{name}
cp -pr tamper %{buildroot}%{_datadir}/%{name}
cp -pr thirdparty %{buildroot}%{_datadir}/%{name}
cp -pr txt %{buildroot}%{_datadir}/%{name}
cp -pr udf %{buildroot}%{_datadir}/%{name}
cp -pr waf %{buildroot}%{_datadir}/%{name}
cp -pr xml %{buildroot}%{_datadir}/%{name}

install -d -m 755 %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/sqlmap <<'EOF'
#!/bin/sh
cd %{_datadir}/%{name}
./sqlmap.py "$@"
EOF
chmod +x %{buildroot}%{_bindir}/sqlmap

install -d -m 755 %{buildroot}%{_sysconfdir}
install -m 644 sqlmap.conf %{buildroot}%{_sysconfdir}
pushd %{buildroot}%{_datadir}/%{name}
ln -s ../../..%{_sysconfdir}/sqlmap.conf .

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py %{buildroot}%{_datadir}/%{name}/*/*/*.py

%files
%doc doc/*
%{_datadir}/%{name}
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9
* Mon Feb 16 2015 guillomovitch <guillomovitch> 1.0-0.20140312.5.mga5
+ Revision: 815250
- add exception for shipped binary exploits
  + umeabot <umeabot>
    - Second Mageia 5 Mass Rebuild
    - Mageia 5 Mass Rebuild
* Wed Mar 19 2014 guillomovitch <guillomovitch> 1.0-0.20140312.2.mga5
+ Revision: 605874
- ship missing modules
* Wed Mar 12 2014 guillomovitch <guillomovitch> 1.0-0.20140312.1.mga5
+ Revision: 602683
- switch to latest development snapshot, as 0.9 is two years old
- fix wrapper script (#12981)
* Fri Oct 18 2013 umeabot <umeabot> 0.9-9.mga4
+ Revision: 502369
- Mageia 4 Mass Rebuild
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Tue Oct 16 2012 guillomovitch <guillomovitch> 0.9-7.mga3
+ Revision: 307152
- switch to Security group
* Tue Aug 23 2011 guillomovitch <guillomovitch> 0.9-6.mga2
+ Revision: 134955
- fix wrapper
- disable automatic dependencies, because of shipped exploits
- this is a noarch package
- stop deleting binaries, they are exploit payloads for the target
- fix wrapper script
- disable automatic svn lookup if pysvn is installed
- drop useless obsoletes tag
  + fwang <fwang>
    - should be arch dependent package
* Wed Jul 20 2011 guillomovitch <guillomovitch> 0.9-1.mga2
+ Revision: 127303
- imported package sqlmap
