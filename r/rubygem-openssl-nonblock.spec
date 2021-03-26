%define debug_package %{nil}

%define rbname openssl-nonblock

Summary:	Non-blocking support for Ruby OpenSSL
Name:		rubygem-%{rbname}
Version:	0.2.1
Release:	7
License:	GPLv2+ or Ruby
Group:		Development/Ruby
Url:		http://rev.rubyforge.org
Source0:	http://gems.rubyforge.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems
BuildRequires:	pkgconfig(openssl)
BuildRequires:	pkgconfig(ruby)

%description
Non-blocking support for Ruby OpenSSL.

%files
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/openssl
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/openssl/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec
%{ruby_sitearchdir}/*.so

#----------------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name}
Group:		Documentation
Requires:	%{name} = %{EVRD}
BuildArch:	noarch

%description doc
Documents, RDoc & RI documentation for %{name}.

%files doc
%doc %{ruby_gemdir}/doc/%{rbname}-%{version}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{rbname}-%{version}

%build
%gem_build

%install
%gem_install


%changelog

* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.2.1-7
- (feb912e) MassBuild#1257: Increase release tag


