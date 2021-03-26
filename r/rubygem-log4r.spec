%global gem_name   log4r
%global gem_dir %{_datadir}/rubygems
%global gem_instdir %{gem_dir}/gems/%{gemname}-%{version}

Name:       rubygem-%{gem_name}
Version:    1.1.10
Release:    10.1
Summary:    Logging framework for ruby
License:    GPLv2
Group:      Development/Ruby
URL:        http://log4r.rubyforge.org
Source0:    http://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby, rubygems
%if 0%{fedora} > 18
BuildRequires: rubypick
%endif
Requires:   rubygems
BuildArch:  noarch

%description
Log4r is a comprehensive and flexible logging library written in Ruby for use
in Ruby programs. It features a hierarchical logging system of any number of
levels, custom level names, logger inheritance, multiple output destinations,
execution tracing, custom formatting, thread safetyness, XML and YAML
configuration, and more.

%package        doc
Summary:    Documentation for %{name}
Group:      Development/Ruby
Requires:   %{name} = %{version}-%{release}

%description    doc
Documents, Rdoc & RI documentation for %{name}.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{gem_dir}
gem install --local --install-dir $RPM_BUILD_ROOT%{gem_dir} \
        --force --rdoc %{SOURCE0}

%files
%{gem_dir}/cache/%{gem_name}-%{version}.gem
%{gem_dir}/gems/%{gem_name}-%{version}
%{gem_dir}/specifications/%{gem_name}-%{version}.gemspec

%files doc
%{gem_dir}/doc/%{gem_name}-%{version}

%changelog
* Sun Dec 24 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.10
- Rebuild for Fedora
* Sat Nov 03 2012 fwang <fwang> 1.1.10-1.mga3
+ Revision: 313158
- new version 1.1.10
* Sun Feb 13 2011 shikamaru <shikamaru> 1.1.9-1.mga1
+ Revision: 51510
- imported package ruby-log4r
