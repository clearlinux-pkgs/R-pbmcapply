#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pbmcapply
Version  : 1.5.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/pbmcapply_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pbmcapply_1.5.0.tar.gz
Summary  : Tracking the Progress of Mc*pply with Progress Bar
Group    : Development/Tools
License  : MIT
Requires: R-pbmcapply-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
the progress of parallel version of vectorized R functions (mc*apply).
  Parallelization (mc.core > 1) works only on *nix (Linux, Unix such as macOS) system due to
  the lack of fork() functionality, which is essential for mc*apply, on Windows.

%package lib
Summary: lib components for the R-pbmcapply package.
Group: Libraries

%description lib
lib components for the R-pbmcapply package.


%prep
%setup -q -c -n pbmcapply
cd %{_builddir}/pbmcapply

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589536977

%install
export SOURCE_DATE_EPOCH=1589536977
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbmcapply
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbmcapply
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pbmcapply
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pbmcapply || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pbmcapply/DESCRIPTION
/usr/lib64/R/library/pbmcapply/INDEX
/usr/lib64/R/library/pbmcapply/LICENSE
/usr/lib64/R/library/pbmcapply/Meta/Rd.rds
/usr/lib64/R/library/pbmcapply/Meta/features.rds
/usr/lib64/R/library/pbmcapply/Meta/hsearch.rds
/usr/lib64/R/library/pbmcapply/Meta/links.rds
/usr/lib64/R/library/pbmcapply/Meta/nsInfo.rds
/usr/lib64/R/library/pbmcapply/Meta/package.rds
/usr/lib64/R/library/pbmcapply/NAMESPACE
/usr/lib64/R/library/pbmcapply/R/pbmcapply
/usr/lib64/R/library/pbmcapply/R/pbmcapply.rdb
/usr/lib64/R/library/pbmcapply/R/pbmcapply.rdx
/usr/lib64/R/library/pbmcapply/help/AnIndex
/usr/lib64/R/library/pbmcapply/help/aliases.rds
/usr/lib64/R/library/pbmcapply/help/paths.rds
/usr/lib64/R/library/pbmcapply/help/pbmcapply.rdb
/usr/lib64/R/library/pbmcapply/help/pbmcapply.rdx
/usr/lib64/R/library/pbmcapply/html/00Index.html
/usr/lib64/R/library/pbmcapply/html/R.css

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/pbmcapply/libs/pbmcapply.so
