Name:           python-scour
Version:	0.26
Release:	2.1
License:	ASL-2.0+
Summary:	An SVG scrubber
URL:		http://www.codedread.com/scour
Group:		System/Libraries
Source:		%{name}-%{version}.tar.bz2
BuildRequires:  python-devel
Provides:	scour = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:	noarch

%description
Scour is an open-source Python script that aggressively cleans SVG files,
removing a lot of 'cruft' that certain tools or authors embed into their
documents. The goal of scour is to provide an identically rendered image.

%prep
%setup -q

%build

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT%{python_sitelib}/scour/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}

%{__mv} scour.py $RPM_BUILD_ROOT%{python_sitelib}/scour/
%{__mv} svg_regex.py $RPM_BUILD_ROOT%{python_sitelib}/scour/
%{__mv} svg_transform.py $RPM_BUILD_ROOT%{python_sitelib}/scour/
%{__mv} yocto_css.py $RPM_BUILD_ROOT%{python_sitelib}/scour/

ln -sf %{python_sitelib}/scour/scour.py $RPM_BUILD_ROOT%{_bindir}/scour

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{python_sitelib}/scour/
%{_bindir}/scour

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.26
- Rebuild for Fedora
* Fri Jan 27 2012 i@marguerite.su
- initial package 0.26
