%global mod_name fpm
%global gem_dir %{_datadir}/rubygems
%global __spec_install_post %{nil}

Name:           rubygem-fpm
Version:        1.14.1
Release:        1
BuildRequires:  ruby, rubygems
BuildRequires:  rubypick
BuildArch:	    noarch
URL:            https://github.com/jordansissel/fpm
Source:         http://rubygems.org/downloads/%{mod_name}-%{version}.gem
Summary:        Package building and mangling
License:        MIT
Group:          Development/Languages/Ruby

%description
Convert directories, rpms, python eggs, rubygems, and more to rpms, debs,
solaris packages and more. Win at package management without wasting pointless
hours debugging bad rpm specs!

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT%{gem_dir} $RPM_BUILD_ROOT%{_bindir}
gem install --local --build-root $RPM_BUILD_ROOT --install-dir %{gem_dir} \
        --force --no-document %{SOURCE0}
ln -s ../share/rubygems/bin/fpm %{buildroot}%{_bindir}/fpm

%files
%{_bindir}/fpm
%{gem_dir}/bin/fpm
%{gem_dir}/cache/%{mod_name}-%{version}.gem
%{gem_dir}/gems/%{mod_name}-%{version}/
%{gem_dir}/specifications/%{mod_name}-%{version}.gemspec

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.14.1
- Rebuilt for Fedora
* Sun Jun  9 2013 coolo@suse.com
- initial package (version 0.4.37)
