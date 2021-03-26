%define realname Xlib

Name:          php-Xlib
Version:       20110911
Release:       2.1
Summary:       X client library written entirely in PHP
Group:         Development/Libraries
License:       opensource
URL:           https://github.com/moriyoshi/php-Xlib
Source0:       moriyoshi-php-Xlib-058ed10.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:     noarch
Requires:      php 

%description
X client library written entirely in PHP.

%prep
%setup -q -n moriyoshi-php-Xlib-058ed10

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/php/%{realname}
install -m 644 * $RPM_BUILD_ROOT%{_datadir}/php/%{realname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/php/%{realname}

%changelog
* Sun Jan 08 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 20110911
- Rebuild for Fedora
