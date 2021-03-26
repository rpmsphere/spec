%global debug_package %{nil}

Name:		java-openjfx
Version:	8.u76
Release:	1.bin
Summary:	OpenJFX runtime libraries
Group:		Development/Languages
License:	GPL with the class path exception
URL:		https://wiki.openjdk.java.net/dashboard.action
Source0:	http://ftp5.gwdg.de/pub/linux/archlinux/extra/os/x86_64/%{name}-%{version}-2-x86_64.pkg.tar.xz
Source1:	http://ftp5.gwdg.de/pub/linux/archlinux/extra/os/i686/%{name}-%{version}-2-i686.pkg.tar.xz
Requires:	jre

%description
OpenJFX is an open source, next generation client application platform for
desktop and embedded systems based on JavaSE. It is a collaborative effort by
many individuals and companies with the goal of producing a modern, efficient,
and fully featured toolkit for developing rich client applications.
This is the open source project where we develop JavaFX.

%global openjdk8dir /usr/lib/jvm/java-1.8.0-openjdk

%prep
%setup -T -c
%ifarch x86_64
tar xf %{SOURCE0}
%else
tar xf %{SOURCE1}
%endif

%build
mv usr/lib/jvm/java-8-openjdk usr/lib/jvm/java-1.8.0-openjdk

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}

%files
%{openjdk8dir}/lib/*
%{openjdk8dir}/bin/*
%{openjdk8dir}/jre/lib/*
%{_mandir}/man1/*

%changelog
* Fri Jun 24 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 8.u76
- Initial binary package
