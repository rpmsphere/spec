%define gemdir %{_datadir}/rubygems
%define gemname fastercsv
%define geminstdir %{gemdir}/gems/%{gemname}-%{version}

Name:		rubygem-%{gemname}
Summary: 	Faster, smaller and cleaner replacement to standard CSV library
Version: 	1.5.5
Release: 	15.1
Group: 		Development/Languages
License: 	GPLv2+ or Ruby
URL:        http://%{gemname}.rubyforge.org/
Source0:    http://rubygems.org/downloads/%{gemname}-%{version}.gem
Requires: 	rubygems
BuildRequires: 	rubypick ruby-devel rubygems
BuildArch: 	noarch
Provides: 	rubygem(%{gemname}) = %{version}

%description
FasterCSV is intended as a complete replacement to the CSV standard library.
It is significantly faster and smaller while still being pure Ruby code. It
also strives for a better interface.

%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{gemdir}
gem install --local --build-root %{buildroot} --install-dir %{gemdir} --force %{SOURCE0}

for file in `find %{buildroot}%{geminstdir} -name "*.rb"`; do
    sed -i 's|/usr/local|/usr|' $file
done

# Remove zero-length file
rm -rf %{buildroot}%{geminstdir}/%{gemname}-%{version}.gem

%clean
rm -rf %{buildroot}

%files
%{gemdir}/gems/%{gemname}-%{version}
%{gemdir}/doc/%{gemname}*
%{gemdir}/cache/%{gemname}-%{version}.gem
%{gemdir}/specifications/%{gemname}-%{version}.gemspec

%changelog
* Tue Feb 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.5
- Rebuild for Fedora
* Tue Jun 4 2013 Sergey Mihailov <sergey.mihailov@gmail.com> - 1.5.5-3
- Initial package
- AutoReqProv no ( missing for Requires: /usr/local/bin/ruby )
