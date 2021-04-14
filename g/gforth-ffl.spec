Name:       gforth-ffl
Version:    0.8.0
Release:    4.1
Summary:    A general purpose Forth library
Group:      Development/Libraries
License:    GPL
URL:		https://github.com/irdvo/ffl
Source0: 	ffl-%{version}.tar.gz
BuildArch:	noarch
Requires:	gforth

%description
The Forth Foundation Library (FFL) is a library written in the Forth
programming language. It contains multiple modules with generally applicable
source code. Its main purpose is to make it easier to develop applications.
 
%prep
%setup -q -n ffl-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}%{_datadir}/gforth/site-forth
cp -a ffl ${RPM_BUILD_ROOT}%{_datadir}/gforth/site-forth

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc examples html test AUTHORS ChangeLog COPYING NEWS README
%{_datadir}/gforth/site-forth/ffl

%changelog
* Sun Nov 11 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.0
- Rebuilt for Fedora
