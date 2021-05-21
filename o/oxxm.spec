Name:		oxxm
Version:	0.1
Release:	2
Summary:	Help Dom0 start up and switch DomU
Summary(zh_TW):	協助虛擬機器 Dom0 開啟與切換 DomU
Group:		Applications
License:	Commercial
Source0:	%{name}-%{version}-ox.tgz
BuildArch:	noarch
Requires:	xen, xen-hypervisor, wmctrl

%description
A shell script for Dom0 used to start up or switch DomU.

%description -l zh_TW
用來協助虛擬機器 Dom0 開啟與切換 DomU 的腳本程式。

%prep
%setup -q

%build
%__make

%install
%__rm -rf $RPM_BUILD_ROOT
%__make install DESTDIR=$RPM_BUILD_ROOT

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc
%{_bindir}/oxxm
%{_sysconfdir}/xen/*.cfg
%{_datadir}/applications/*.desktop
%{_datadir}/applications/icons/OSSII-icons/scalable/apps/*.png

%post
update-desktop-database %{_datadir}/applications >/dev/null 2&1 || :

%postun
update-desktop-database %{_datadir}/applications >/dev/null 2&1 || :

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuilt for Fedora
* Wed Dec 31 2010 Chih-Chun Tu <vincent.tu@ossii.com.tw> 0.1-2
- Add new function to check DomU disk image file exist or not.

* Wed Dec 23 2010 Chih-Chun Tu <vincent.tu@ossii.com.tw> 0.1-1
- Build the program.

