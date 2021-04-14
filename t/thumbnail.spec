Name:			thumbnail
Summary:		Creates thumbail images
Version:		0.4
Release:		5.1
License:		GPL
Group:			Productivity/Graphics/Convertors
URL:			http://www.chaosreigns.com/code/thumbnail/
Source:			%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch
Requires:		perl
Requires:		ImageMagick

%description
Creates a thumbnail image upto a maximum size of 10000 (100x100) pixels.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -D -m755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc COPYING INSTALL

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuilt for Fedora
