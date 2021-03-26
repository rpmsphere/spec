%global debug_package %{nil}

Name:          quota-tools
Version:       3.17
Release:       3.1
Summary:       User space tools for the Linux Diskquota system
Group:         System/Tools
URL:           http://sourceforge.net/projects/linuxquota/
Source:        http://switch.dl.sourceforge.net/sourceforge/linuxquota/quota-%{version}.tar.gz
License:       GPL
BuildRequires: gettext-devel
BuildRequires: tcp_wrappers-devel

%description
User space tools for the Linux Diskquota system as part of the Linux kernel.

%prep
%setup -q -n quota-tools

%build
%configure --sysconfdir=%{_sysconfdir}/quota
make

%install
make DESTDIR=$RPM_BUILD_ROOT install ROOTDIR=%{buildroot}
#sysconfdir=$RPM_BUILD_ROOT%{_sysconfdir}/quota

# delete headers because they are already in glibc-devel
rm -f $RPM_BUILD_ROOT%{_includedir}/rpcsvc/* 
mv $RPM_BUILD_ROOT%{_mandir}/man2/quotactl.2 %{buildroot}%{_mandir}/man2/quotactl-quotatools.2

%find_lang quota

%clean
rm -rf $RPM_BUILD_ROOT

%files -f quota.lang
%{_sbindir}/*
%{_bindir}/*
%dir %{_sysconfdir}/quota
%{_sysconfdir}/quota/*
%{_mandir}/man1/*
%{_mandir}/man2/*
%{_mandir}/man3/*
%{_mandir}/man8/*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.17
- Rebuild for Fedora
* Tue Jan 27 2009 Silvan Calarco <silvan.calarco@mambasoft.it> 3.17-1mamba
- automatic update by autodist
* Fri Sep 21 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 3.15-1mamba
- update to 3.15
* Wed May 06 2004 Silvan Calarco <silvan.calarco@mambasoft.it> 3.11-1qilnx
- first build
