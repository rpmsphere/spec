Name:		mdf2iso
Version:	0.3.0
Release:	5.1
License:	GPL
Summary:	Convert Alkohl 120% CD Images to ISO
Group:		System
Source:		%{name}-%{version}-src.tar.bz2	
BuildRequires:	gcc

%description
MDF2ISO is a very simple utility to convert an Alcohol 120% bin image
to the standard ISO-9660 format.

%prep
%setup -q -n %{name}

%build
touch INSTALL
touch NEWS
touch README
touch AUTHORS
touch COPYING
aclocal
autoconf
automake --add-missing
./configure --prefix=/usr
%__make %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{makeinstall}

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog gpl.txt
%{_bindir}/%{name}

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.0
- Rebuild for Fedora
* Tue Jan 26 2008 TI_Eugene <ti.eugene@gmail.com> 0.3.0-%{?dist}
- Initial release for openSUSE Build Service
