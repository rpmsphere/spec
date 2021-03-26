Name     : python3-keras
Version  : 2.2.4
Release  : 1
URL      : https://keras.io/
Source0  : https://github.com/keras-team/keras/archive/2.2.4.tar.gz#/Keras-%{version}.tar.gz
Summary  : The Python Deep Learning library
Group    : Development/Tools
License  : MIT
Requires: Keras-python3
Requires: Keras-license
Requires: Keras-python
Requires: Keras_Applications
Requires: Keras_Preprocessing
Requires: PyYAML
Requires: h5py
Requires: numpy
Requires: pandas
Requires: pydot
Requires: pytest-timeout
Requires: requests
Requires: scipy
Requires: six
BuildArch: noarch

%description
Keras is a high-level neural networks API, written in Python and
capable of running on top of TensorFlow, CNTK, or Theano. It was
developed with a focus on enabling fast experimentation.

%prep
%setup -q -n Keras-%{version}

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538616514
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/Keras
cp LICENSE %{buildroot}/usr/share/doc/Keras/LICENSE
python3 setup.py install --root=%{buildroot}
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :

%files
%license /usr/share/doc/Keras/LICENSE
%doc README.md CONTRIBUTING.md examples
%{python3_sitelib}/*

%changelog
* Mon Jan 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.4
- Rebuild for Fedora
