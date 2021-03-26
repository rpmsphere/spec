Name:          jrnl
Version:       1.9.8
Release:       3.1
License:       MIT
Summary:       Collect your thoughts and notes without leaving the command line
URL:           http://maebert.github.io/jrnl/
Group:         Productivity/Office/Organizers
Source0:       jrnl-%{version}.tar.gz
Patch0:        fix-python-dateutil-requirement.patch
BuildRequires: python2-setuptools
Requires:      python-dateutil
Requires:      python-keyring
Requires:      python-parsedatetime
Requires:      python-pycrypto
Requires:      python-pytz
Requires:      python-six
Requires:      python-tzlocal
Requires:      python2-setuptools
BuildArch:     noarch
Provides:      python-jrnl

%description
jrnl is a simple journal application for your command line. Journals are stored
as human readable plain text files - you can put them into a Dropbox folder for
instant syncing and you can be assured that your journal will still be readable
in 2050, when all your fancy iPad journal applications will long be forgotten.

%prep
%setup -q
%patch0

%build
python2 setup.py build

%install
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE README.md CHANGELOG.md
%{_bindir}/jrnl
%{python_sitelib}/jrnl*

%changelog
* Fri Jun 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9.8
* Fri Jul 10 2015 jkeil@suse.de
- Fix service file for Factory
* Fri Jul 10 2015 jkeil@suse.de
- Fix service file
* Fri Jul 10 2015 jkeil@suse.de
- python2-setuptools is also a runtime dependency
* Tue Jun  9 2015 jkeil@suse.de
- Initial python-jrnl package
