Name:		oxpackage
Version:	0.3
Release:	2
Summary:	Installer for .oxpkgs file
Summary(zh_TW):	.oxpkgs 檔安裝程式
Group:		Applications
License:	Commercial
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	oxzilla >= 0.1.1-19, yum, zenity

%description
A shell script used to install the packages recorded 
within .oxpkgs file

%description -l zh_TW
用來安裝紀錄在 .oxpkgs 檔案內套件的腳本程式。

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
%{_bindir}/*
%{_datadir}/mime/packages/*.xml
%{_datadir}/applications/*.desktop

%post
update-mime-database %{_datadir}/mime/ &> /dev/null || :
update-desktop-database &> /dev/null || :

%postun
update-mime-database %{_datadir}/mime/ &> /dev/null || :
update-desktop-database &> /dev/null || :

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Wed Dec 7 2010 Chih-Chun Tu <vincent.tu@ossii.com.tw> 0.3-2
- Remove the queuing window of packages
- Add the information window of packages after clicking the downloading button

* Wed Dec 1 2010 Chih-Chun Tu <vincent.tu@ossii.com.tw> 0.3-1
- Add the queuing function

* Tue Oct 13 2010 Wei-Lun Chao <bluebat@member.fsf.org> 0.2-2
- Add oxstore.desktop

* Mon Aug 9 2010 Huan-Ting Luo <kylix@ossii.com.tw> 0.1-3
- fix the presentation of the package installing when progressing

* Fri Aug 6 2010 Huan-Ting Luo <kylix@ossii.com.tw> 0.1-2
- fix the format of date within install.log
- fix the presentation of the result of .oxpkgs file installation

* Thu Aug 5 2010 Huan-Ting Luo <kylix@ossii.com.tw> 0.1-1
- build the program
