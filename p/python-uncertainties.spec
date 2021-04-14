%define __python /usr/bin/python2
%define pyname uncertainties

Name:           python-uncertainties
Version:        3.0.2
Release:        3.1
Summary:        Transparent calculations with uncertainties
License:        GPL-2
URL:            http://packages.python.org/uncertainties/
Group:          Development/Libraries/Python
Source:         https://pypi.python.org/packages/source/u/uncertainties/%{pyname}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools

%description
Transparent calculations with uncertainties on the quantities involved (aka
"error propagation"); calculation of derivatives uncertainties allows
calculations such as (2 +/- 0.1)*2 = 4 +/- 0.2 to be performed transparently;
much more complex mathematical expressions involving numbers with uncertainty
can also be evaluated directly.

Correlations between expressions are correctly taken into account. x-x is thus
exactly zero, for instance (most implementations found on the web yield a
non-zero uncertainty for x-x, which is incorrect).

%prep
%setup -n %{pyname}-%{version}

# fix some exec bits
find . -name "*.py" -exec chmod -x '{}' \;

# Remove shebang
for file in `find . -name "*.py"`; do
        sed '/^#!\//, 1d' $file > $file.new && \
        touch -r $file $file.new && \
        mv $file.new $file
done

%build
%{__python} setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=$RPM_BUILD_ROOT

%files
%doc README.rst LICENSE.txt
%{python_sitelib}/*

%changelog
* Wed Jan 17 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.2
- Rebuilt for Fedora
* Sun Dec  4 2011 ocefpaf@gmail.com
- updated to revision 418
* Sat Oct 29 2011 ocefpaf@gmail.com
- updated to revision 397; version 1.8
* Sun Jul 10 2011 ocefpaf@yahoo.com.br
- updated to revision 383; version 1.7.4
* Sat Jun 25 2011 ocefpaf@yahoo.com.br
- updated to release 374; version 1.7.3
* Sun May  1 2011 ocefpaf@yahoo.com.br
- updated to release 359; version 1.7.2
* Sat Mar 19 2011 ocefpaf@yahoo.com.br
- updated to 1.7.1
* Sun Oct 24 2010 ocefpaf@yahoo.com.br
- first release
- specfile cleanup
- updated to 1.7
