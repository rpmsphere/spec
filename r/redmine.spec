Name:           redmine
Version:        4.1.1
Release:        1
Summary:        A flexible project management web application
Group:          Networking/WWW
License:        GPLv2+
URL:            http://www.redmine.org
Source0:        http://www.redmine.org/releases//%{name}-%{version}.tar.gz
Source101:      %{name}.logrotate
Source102:      %{name}.apache24
Source103:      %{name}-pg-database.yml
#BuildRequires:  ruby >= 1.8.7
#BuildRequires:  ruby-RubyGems
#BuildRequires:	ruby-fastercsv
Requires:       webserver
Requires:       rubygem-rails >= 4.0.1
Requires:       rubygems
Requires:       %{name}-db
Requires:       rubygem-bigdecimal
Requires:       rubygem(jquery-rails) >= 2.0.2
Requires:       rubygem(i18n) >= 0.6.6
Requires:       rubygem(coderay) >= 1.0.9
Requires:       rubygem(fastercsv) >= 1.5.0
Requires:       rubygem(builder) => 3.0.0
Requires:       rubygem-database_cleaner
# Only suggests rubygem-passenger, after all, it can work with fcgi too
Suggests:       rubygem-passenger
Suggests:       ruby-RMagick
Suggests:       rubygem-ruby-openid
Suggests:       %{name}-scm
Suggests:       ruby-rack-openid
Suggests:       ruby-selenium-webdriver
Suggests:       ruby-actionpack
Suggests:       ruby-net-ldap
Suggests:       ruby-yard
Suggests:       ruby-shoulda
Suggests:       ruby-mocha
Suggests:       ruby-capybara
Suggests:       ruby-protected_attributes
Suggests:       ruby-actionpack-action_caching
BuildArch:      noarch

%description
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

Overview

 * Multiple projects support
 * Flexible role based access control
 * Flexible issue tracking system
 * Gantt chart and calendar
 * News, documents & files management
 * Feeds & email notifications
 * Per project wiki
 * Per project forums
 * Time tracking
 * Custom fields for issues, time-entries, projects and users
 * SCM integration (SVN, CVS, Git, Mercurial, Bazaar and Darcs)
 * Issue creation via email
 * Multiple LDAP authentication support
 * User self-registration support
 * Multilanguage support
 * Multiple databases support

%package pg
Summary:        A flexible project management web application - pgsql connector
Group:          Networking/WWW
Requires:       rubygem-pg
Provides:       %{name}-pg = %{version}-%{release}
Provides:       %{name}-db = %{version}-%{release}

%description pg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use postgresql as redmine's
database backend.

%files pg
%{_var}/www/%{name}/config/database.postgres.yml

%package mysql
Summary:        A flexible project management web application - mysql connector
Group:          Networking/WWW
Requires:       rubygem-mysql2
Provides:       %{name}-mysql = %{version}-%{release}
Provides:       %{name}-db    = %{version}-%{release}

%description mysql
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mysql as redmine's
database backend.

%files mysql
%config(noreplace) %{_var}/www/%{name}/config/database.yml

%package sqlite
Summary:        A flexible project management web application - sqlite connector
Group:          Networking/WWW
Requires:       rubygem-sqlite3
Provides:       %{name}-sqlite = %{version}-%{release}
Provides:       %{name}-db     = %{version}-%{release}

%description sqlite
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use sqlite as redmine's
database backend.

%files sqlite

%package git
Summary:        A flexible project management web application - git backend
Group:          Networking/WWW
Requires:       git-core
Provides:       %{name}-git = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description git
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use git as redmine's
version control system backend

%files git

%package svn
Summary:        A flexible project management web application - subversion backend
Group:          Networking/WWW
Requires:       subversion
Provides:       %{name}-svn = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description svn
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use subversion as redmine's
version control system backend


%files svn

%package hg
Summary:        A flexible project management web application - mercurial backend
Group:          Networking/WWW
Requires:       mercurial
Provides:       %{name}-hg  = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description hg
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use mercurial as redmine's
version control system backend

%files hg

%package bzr
Summary:        A flexible project management web application - bzr backend
Group:          Networking/WWW
Requires:       bzr
Provides:       %{name}-bzr = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description bzr
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use bazaar as redmine's
version control system backend

%files bzr

%package cvs
Summary:        A flexible project management web application - cvs backend
Group:          Networking/WWW
Requires:       cvs
Provides:       %{name}-cvs = %{version}-%{release}
Provides:       %{name}-scm = %{version}-%{release}

%description cvs
Redmine is a flexible project management web application. Written using
Ruby on Rails framework, it is cross-platform and cross-database.

This package contains the needed modules to use cvs as redmine's
version control system backend

%files cvs

%prep
%setup -q

# Remove the backup patch files as the install is done with cp *
rm -f *.00??

%build
find . -name ".gitignore" -exec rm {} \;

%install
install -d %{buildroot}%{_var}/www/%{name}
cp -rf * %{buildroot}%{_var}/www/%{name}

# Don’t include bundled rails
rm -rf %{buildroot}%{_var}/www/%{name}/vendor/rails

# Don't include some prebuilt binaries
rm -rf %{buildroot}%{_var}/www/%{name}/lib/plugins/rfpdf/lib/fonts/ttf2ufm

# Copy database.yml.example as it’s mandatory to run redmine
cp %{buildroot}%{_var}/www/%{name}/config/database.yml.example %{buildroot}%{_var}/www/%{name}/config/database.yml
# Likewise, add postgresql conf
install -D -m644 %{SOURCE103} %{buildroot}%{_var}/www/%{name}/config/database.postgres.yml

# Add Logrotate script
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -D -m644 %{SOURCE101} %{buildroot}%{_sysconfdir}/logrotate.d/%{name}

# Add httpd default conf
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d/
install -D -m644 %{SOURCE102} %{buildroot}%{_sysconfdir}/httpd/conf/vhosts.d/%{name}.conf

%files
%{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf/vhosts.d/%{name}.conf
%doc %{_var}/www/%{name}/README.rdoc
%doc %{_var}/www/%{name}/CONTRIBUTING.md
%dir %{_var}/www/%{name}/
%{_var}/www/%{name}/app/
%dir %{_var}/www/%{name}/config/
%doc %{_var}/www/%{name}/config/*.example
%{_var}/www/%{name}/config/environments/
%{_var}/www/%{name}/config/locales/
%{_var}/www/%{name}/config/initializers/
%{_var}/www/%{name}/config/routes.rb
%{_var}/www/%{name}/config/boot.rb
%{_var}/www/%{name}/config/environment.rb
%{_var}/www/%{name}/config/settings.yml
%{_var}/www/%{name}/db/
%{_var}/www/%{name}/doc/
%{_var}/www/%{name}/extra/
# Directory has to be owned by the user under which the webserver runs
# Since apache is the preferred webserver for many people simplify the
# process for those users, but it sucks, all webservers should belong
# to the same user :-(
%attr(0755,apache,apache) %{_var}/www/%{name}/files/
%{_var}/www/%{name}/lib/
%attr(0755,apache,apache) %{_var}/www/%{name}/log/
%{_var}/www/%{name}/public/
%{_var}/www/%{name}/Rakefile
#%{_var}/www/%{name}/script/
%{_var}/www/%{name}/test/
%attr(0755,apache,apache) %{_var}/www/%{name}/tmp/
%{_var}/www/%{name}/vendor/
%{_var}/www/%{name}/Gemfile
%{_var}/www/%{name}/config.ru
%{_var}/www/%{name}/config/application.rb
#{_var}/www/%{name}/config/preinitializer.rb
%{_var}/www/%{name}/plugins/README
%{_var}/www/%{name}/bin/
%{_var}/www/redmine/appveyor.yml

%changelog
* Fri May 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 4.1.1
- Rebuild for Fedora
* Mon Dec 30 2013 pterjan <pterjan> 2.4.2-1.mga4
+ Revision: 563254
- Update rails patch to accept 4.0.2
- From Mika Laitio <lamikr@pilppa.org>
 + update to redmine 2.4.2
 + add rails 4.0.1 compatibility patches because 2.3.3 and 2.4.2 do
   not work with rails 4 by default
 + update download url to redmine releases
* Thu Dec 26 2013 pterjan <pterjan> 2.3.3-4.mga4
+ Revision: 560878
- Update dependencies based on Gemfile
* Thu Dec 26 2013 pterjan <pterjan> 2.3.3-3.mga4
+ Revision: 560872
- Add missing Requires on ruby-bigdecimal
* Tue Oct 22 2013 umeabot <umeabot> 2.3.3-2.mga4
+ Revision: 545047
- Mageia 4 Mass Rebuild
* Tue Oct 15 2013 zezinho <zezinho> 2.3.3-1.mga4
+ Revision: 500713
- apache conf file
- new version
- supports ruby >= 2.0
- apache conf file updated for apache 2.4
* Sat May 04 2013 pterjan <pterjan> 2.2.4-1.mga3
+ Revision: 412293
- Drop prebuilt binaries of ttf2ufm, this avoids a crash in find-debuginfo.sh
- Don't try to modify a file from another package at build time
  + spuhler <spuhler>
    - upgrade to version 2.2.4
     - Redmine 2.2.4 is a maintenance release for the 2.2.x branch that fixes a few issues
     - Redmine 2.2.4 has been upgraded to Rails 3.2.13 which fixes several security vulnerabilities
      added BuildRequires: ruby-fastercsv
      corrected location of lib/faster_csv.rb
  + fwang <fwang>
    - new version 2.2.3
    - remove in-exist req
  + umeabot <umeabot>
    - Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sat Dec 22 2012 kamil <kamil> 2.2.0-1.mga3
+ Revision: 333931
- don't use full URL in Source0
- new version 2.2.0
* Tue May 29 2012 kamil <kamil> 2.0.1-1.mga3
+ Revision: 248952
- new version 2.0.1
* Sun Apr 08 2012 fwang <fwang> 1.3.2-1.mga2
+ Revision: 229671
- new version 1.3.2
  + kamil <kamil>
    - new version 1.3.0
    - drop P0 (no more needed)
  + shikamaru <shikamaru>
    - Rebuild for new rails
    - add patch for rails compatibility
    - retab spec
    - bump release
* Wed Jun 22 2011 dams <dams> 1.2.0-3.mga2
+ Revision: 112455
+ rebuild (emptylog)
* Wed Jun 22 2011 dams <dams> 1.2.0-2.mga2
+ Revision: 112434
- Add 'ruby-ruby-devel' as a require
* Tue Jun 21 2011 dams <dams> 1.2.0-1.mga2
+ Revision: 111254
- add 'rubygems' as BR
- add 'ruby' as BR
- Update to 1.2.0
- Remove patch0 as it's now useless
- imported package redmine
* Sun Nov 14 2010 Thierry Vignaud <tv@mandriva.org> 1.0.3-8mdv2010.1
+ Revision: 597532
- description != license
* Sun Nov 14 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.3-7mdv2011.0
+ Revision: 597523
- add rails and rack as dependency since we don't enforce passenger
- add patch to fix rails version in environment.rb
* Sun Nov 14 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.3-6mdv2011.0
+ Revision: 597503
- Ease integration
- add default database.yml file and provide an example for pgsql
- provide default apache configuration
- only suggests rubygem-passenger to allow other webservers that can
   work in cgi/fcgi mode
- change the permissions for folders that have to be owned by the
  webserver (only ease the processe for apache atm :/)
- fix rubygem-pg dependency
- do not include bundled rails
* Sat Nov 13 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.3-4mdv2011.0
+ Revision: 597185
- Add logrotate file and fix subpackages description
* Wed Nov 03 2010 Rémy Clouard <shikamaru@mandriva.org> 1.0.3-2mdv2011.0
+ Revision: 592854
- fix build
- import redmine
