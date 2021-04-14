%define pyname pyreport

Name:           python2-%{pyname}
Version:        0.3.4c
Release:        22.1
Summary:        Pyreport makes notes out of a python2 script
License:        BSD
Group:          Development/Libraries/Python
URL:            http://gael-varoquaux.info/computers/pyreport/
Source0:        %{pyname}-%{version}.tar.bz2
Patch0:         pyplot_silent.diff
BuildArch:      noarch
BuildRequires:  python2-devel, python2-setuptools, fdupes
Requires:       docutils

%description
Pyreport makes notes out of a python script. It can run the script in a sandbox
and capture its output. It allows for embedding RestructuredText or LaTeX
comments in the code for literate programming and generates a report made of the
literate comments, the code, pretty printed, and the output of the script
(pyreport can capture pylab figures). This is useful for do cumentations, making
tutorials, but also for sharing python-based calculations with colleagues.

%prep
%setup -q -n %{pyname}-%{version}
%patch0 -p1

%build
# Build an egg file that we can then install from
CFLAGS="%{optflags} " python2 setup.py bdist_egg

%install
rm -rf $RPM_BUILD_ROOT

# Install the egg so that only code that wants this version can get it.
#mkdir -p $RPM_BUILD_ROOT%{python2_sitelib}
easy_install-2.7 -m --prefix $RPM_BUILD_ROOT%{_usr} dist/*.egg

# remove byte-compiling until I figure out:
# "Your file contains traces of $RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT/%{python2_sitelib} -name "*.pyc" -exec rm -f '{}' \;

# fix some exec bits
#find $RPM_BUILD_ROOT/%{python2_sitelib} -name "*.py" -exec chmod -x '{}' \;
#chmod +x $RPM_BUILD_ROOT/%{python2_sitelib}/%{pyname}-%{version}-py*.egg/%{pyname}/pyreport.py

%files
%{python2_sitelib}/*
%{_bindir}/%{pyname}

%changelog
* Mon Dec 26 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.4c
- Rebuilt for Fedora
* Sun Mar 20 2011 ocefpaf@yahoo.com.br
- specfile cleanup
* Thu Aug  5 2010 Filipe Fernandes <ocefpaf@gmail.com> - 0.3.4c
- added a patch to fix --silent option and pyplot plt.show()
* Wed Aug  4 2010 Filipe Fernandes <ocefpaf@gmail.com> - 0.3.4c
- clean up spec file
- remove .pyc, when using easy_install the pyc contains traces of %%$RPM_BUILD_ROOT
* Mon Feb 15 2010 Filipe Fernandes <ocefpaf@gmail.com> - 0.3.4c
- updated tp 0.3.4c
* Sat Nov 14 2009 Filipe Fernandes <ocefpaf@gmail.com> - 0.3.4b
- first release
