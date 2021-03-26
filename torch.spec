Name:			torch
Version:		3.1
Release:		5.1
Summary:		A simple machine-learning library	
Group:			Engineering
License:		BSD
URL:			http://www.torch.ch/
Source0:		http://www.torch.ch/archives/Torch3src.tgz
Source1:		http://www.torch.ch/archives/Torch3doc.tgz
Source44:		import.info
BuildRequires:		gcc-c++

%description
Among its features you can find:
* A lot of things in gradient machines, that is, machines which could be
  learned with a gradient descent. This includes multi-layered perceptrons,
  radial bas is functions, mixtures of experts, convolutional networks and
  even time-delay neural networks. In fact a lot of "modules" are available
  that you can plug as you want to get what you need.
* Support vector machines, in classification and regression. As fast as the
  old stand-alone program SVMTorch II, but with the powerful environment of
  the library.
* Ensemble models such as bagging or adaboost.
* Non-parametric models such as K-nearest-neighbors, Parzen regression and
  Parzen density estimator.
* Distributions stuff, like Kmeans, Gaussian mixture models, hidden Markov
  models, input-output hidden Markov models, and Bayes classifier.
* Speech recognition tools (Embedded training and large vocabulary decoding).

%package devel
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{name} = %{version}-%{release}

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n Torch3

# fix utf8
iconv -f ISO-8859-2 -t UTF-8 LICENSE > LICENSE.utf8
mv LICENSE.utf8 LICENSE
rm examples/LICENSE

# extract the docs
tar xzvf %{SOURCE1}

%build
ln -s config/Makefile_options_Linux .
# use default gcc flags
sed -i -e "s|CFLAGS_OPT_DOUBLE = -Wall -O2 -ffast-math -mcpu=i686 -march=i686 -malign-double -DUSE_DOUBLE|CFLAGS_OPT_DOUBLE = -DUSE_DOUBLE %{optflags} -fPIC -DPIC|" \
-e "s|CFLAGS_OPT_FLOAT = -Wall -O2 -ffast-math -mcpu=i686 -march=i686 -malign-double|CFLAGS_OPT_FLOAT = %{optflags} -fPIC -DPIC|" Makefile_options_Linux
# add all packages to be built
sed -i "s|PACKAGES =|PACKAGES = convolutions datasets decoder distributions gradients kernels matrix nonparametrics speech|" Makefile_options_Linux
# we DO want to see what's going on during the build
find . -name Makefile -exec sed -i 's|@$(CC) $(CFLAGS_$(MODE)) $(INCS) -o $@ -c $<|$(CC) $(CFLAGS_$(MODE)) $(INCS) -o $@ -c $<|' {} \;
# remove any exit() calls from library's code
sed -i '/exit(-1);/d' core/{CmdLine.cc,general.cc}
sed -i 's/exit (-1);/return NULL;/' datasets/IOHTK.cc
# do not build a static library...
sed -i "s/AR = ar -rus/AR = :/" Makefile_options_Linux

make depend
make %{?_smp_mflags}

# ...but make a shared one
g++ %{optflags} -shared -Wl,-soname,libtorch.so.1 -o libtorch.so.1.0.0 `find . -name "*.o"`

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}
mkdir -p $RPM_BUILD_ROOT%{_includedir}/torch

# install the library
install -p -m 755 libtorch.so.1.0.0 $RPM_BUILD_ROOT%{_libdir}
pushd $RPM_BUILD_ROOT%{_libdir}
	ln -sf libtorch.so.1.0.0 libtorch.so.1
	ln -sf libtorch.so.1.0.0 libtorch.so
popd

# install the headers
find . -name "*.h" -exec install -p -m 644 {} $RPM_BUILD_ROOT%{_includedir}/torch \;

%files devel
%{_includedir}/torch
%{_libdir}/libtorch.so
%doc examples docs

%files
%doc ChangeLog LICENSE
%{_libdir}/libtorch.so.1.0.0
%{_libdir}/libtorch.so.1

%changelog
* Thu Jul 12 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuild for Fedora
* Mon Oct 19 2015 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_12
- update to new release by fcimport
* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_10
- update to new release by fcimport
* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_9
- update to new release by fcimport
* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_8
- update to new release by fcimport
* Mon Apr 29 2013 Igor Vlasenko <viy@altlinux.ru> 3.1-alt1_7
- initial fc import
