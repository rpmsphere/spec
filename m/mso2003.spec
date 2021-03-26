Name:		mso2003
Version:	11.6568.5606SC
Release:	2%{?dist}.bin
Summary:	Microsoft Office 2003
Source0:	msoffice_11.6568.5606-2_all.deb
URL:		http://microsoft.com/
Group:		Applications/Productivity
BuildArch:	noarch
License:	commercial
BuildRoot:	%{_tmppath}/build-%{name}-%{version}
Requires:	wine, openal-soft

%description
Microsoft Office 2003 Simplified Chinese Version. 
Including word, excel and powerpoint.

%prep
%setup -T -c
ar -x %{SOURCE0}

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}
tar xzvf data.tar.gz -C %{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/ms*
%{_datadir}/applications/ms*.desktop
%{_datadir}/pixmaps/ms*.xpm
/opt/wine/%{name}

%changelog
* Fri Oct 08 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Initial package
