#
# Spec file for CVC4 packages.
#
Summary: First order formula validity checker (version 4)
Name: cvc4
Version: 1.2
Release: 1
License: BSD
Source: http://cvc4.cs.nyu.edu/builds/src/cvc4-1.2.tar.gz
Patch0: cvc4-rpm.patch
URL: http://cvc4.cs.nyu.edu/
BuildRequires: gmp-devel, zlib-devel, doxygen, graphviz, antlr3-C-devel >= 3.2, boost-devel, readline-devel, swig >= 2.0, java-sdk
# for other language bindings: python-devel, perl-devel, ruby-devel, tcl-devel, php-devel
Conflicts: cvc4-nightly
Packager: Morgan Deters <mdeters@cs.nyu.edu>

%package devel
Summary: First order formula validity checker (version 4), development files
%package java
Summary: First order formula validity checker (version 4), Java bindings
%package doc
Summary: First order formula validity checker (version 4), documentation

%description
This package contains the CVC4 binaries and shared libraries.

CVC4 is a tool for determining the satisfiability of a first order formula
modulo a first order theory (or a combination of such theories). It is the
fourth in the Cooperating Validity Checker family of tools (CVC, CVC Lite,
CVC3) but does not directly incorporate code from any previous version.

CVC4 is intended to be an open and extensible SMT engine. It can be used
as a stand-alone tool or as a library. It has been designed to increase
the performance and reduce the memory overhead of its predecessors.

%description devel
This is the CVC4 development package, containing headers and static
libraries for CVC4.  Install this package only if you need to build
packages from source that depend on the CVC4 library API.

CVC4 is a tool for determining the satisfiability of a first order formula
modulo a first order theory (or a combination of such theories). It is the
fourth in the Cooperating Validity Checker family of tools (CVC, CVC Lite,
CVC3) but does not directly incorporate code from any previous version.

CVC4 is intended to be an open and extensible SMT engine. It can be used
as a stand-alone tool or as a library. It has been designed to increase
the performance and reduce the memory overhead of its predecessors.

%description java
This package contains the CVC4 Java bindings.  "CVC4.so" and "CVC4.jar"
contain the Java API that allows CVC4 to support Java programs.

CVC4 is a tool for determining the satisfiability of a first order formula
modulo a first order theory (or a combination of such theories). It is the
fourth in the Cooperating Validity Checker family of tools (CVC, CVC Lite,
CVC3) but does not directly incorporate code from any previous version.

CVC4 is intended to be an open and extensible SMT engine. It can be used
as a stand-alone tool or as a library. It has been designed to increase
the performance and reduce the memory overhead of its predecessors.

%description doc
This package contains CVC4 documentation.

CVC4 is a tool for determining the satisfiability of a first order formula
modulo a first order theory (or a combination of such theories). It is the
fourth in the Cooperating Validity Checker family of tools (CVC, CVC Lite,
CVC3) but does not directly incorporate code from any previous version.

CVC4 is intended to be an open and extensible SMT engine. It can be used
as a stand-alone tool or as a library. It has been designed to increase
the performance and reduce the memory overhead of its predecessors.

%prep
%setup -q
%patch0 -p1

%build
%configure --enable-static --enable-shared --with-build=default --enable-language-bindings=c,java --with-gmp --with-compat --with-readline --with-portfolio --disable-doxygen-pdf --enable-doxygen-dot JAVA_CPPFLAGS='-I/usr/lib/jvm/java/include -I/usr/lib/jvm/java/include/linux'
# configure --enable-static --enable-shared --with-build=default --with-portfolio --enable-language-bindings=c,java,tcl,ruby,php,perl,python --with-gmp --with-compat --with-readline --with-portfolio --disable-doxygen-pdf --enable-doxygen-dot
# PERL_CPPFLAGS=-I/usr/lib/perl/5.12/CORE/ PHP_CPPFLAGS='-I/usr/include/php5/Zend -I/usr/include/php5/TSRM -I/usr/include/php5/main -I/usr/include/php5' PYTHON_CPPFLAGS=-I/usr/include/python2.7 RUBY_CPPFLAGS=-I/usr/lib/ruby/1.8/x86_64-linux TCL_CPPFLAGS=-I/usr/include/tcl8.5
make %{?_smp_mflags}

%check
# Skip unit tests (by doing a "make regress" instead of "make check") to avoid a
# build dependency on CxxTest
make %{?_smp_mflags} regress

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
# incorrectly installed by "make install" in some versions
rm -f %{buildroot}%{_includedir}/cvc4/cvc4_private_library.h
# don't care about static or libtool versions of these
rm -f %{buildroot}%{_libdir}/jni/libcvc4compatjni.a
rm -f %{buildroot}%{_libdir}/jni/libcvc4compatjni.la
rm -f %{buildroot}%{_libdir}/jni/libcvc4jni.a
rm -f %{buildroot}%{_libdir}/jni/libcvc4jni.la
rm -f %{buildroot}%{_libdir}/jni/libcvc4jni.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING RELEASE-NOTES NEWS README AUTHORS THANKS
%{_bindir}/cvc4
%{_bindir}/pcvc4
%{_libdir}/libcvc4.so.*
%{_libdir}/libcvc4parser.so.*
%{_libdir}/libcvc4compat.so.*
%{_libdir}/libcvc4bindings_c_compat.so.*
%doc %{_mandir}/man1/cvc4.1.gz
%doc %{_mandir}/man1/pcvc4.1.gz
%doc %{_mandir}/man5/cvc4.5.gz

%files devel
%defattr(-,root,root,-)
%{_includedir}/cvc4/context
%{_includedir}/cvc4/cvc4.h
%{_includedir}/cvc4/cvc4_public.h
%{_includedir}/cvc4/decision
%{_includedir}/cvc4/expr
%{_includedir}/cvc4/lib
%{_includedir}/cvc4/main
%{_includedir}/cvc4/printer
%{_includedir}/cvc4/proof
%{_includedir}/cvc4/prop
%{_includedir}/cvc4/smt
%{_includedir}/cvc4/theory
%{_includedir}/cvc4/util
%{_includedir}/cvc4/options
%{_libdir}/libcvc4.a
%{_libdir}/libcvc4.so
%{_libdir}/libcvc4.la
%doc %{_mandir}/man3/libcvc4.3.gz
%doc %{_mandir}/man3/SmtEngine.3cvc.gz
%doc %{_mandir}/man3/options.3cvc.gz
%{_includedir}/cvc4/cvc4parser_public.h
%{_includedir}/cvc4/parser
%{_libdir}/libcvc4parser.a
%{_libdir}/libcvc4parser.so
%{_libdir}/libcvc4parser.la
%doc %{_mandir}/man3/libcvc4parser.3.gz
%{_includedir}/cvc4/compat
%{_libdir}/libcvc4compat.a
%{_libdir}/libcvc4compat.so
%{_libdir}/libcvc4compat.la
%doc %{_mandir}/man3/libcvc4compat.3.gz
%{_includedir}/cvc4/bindings/compat/c
%{_libdir}/libcvc4bindings_c_compat.a
%{_libdir}/libcvc4bindings_c_compat.so
%{_libdir}/libcvc4bindings_c_compat.la

%files java
%defattr(-,root,root,-)
%{_libdir}/jni/libcvc4jni.so*
%{_datadir}/java/CVC4.jar
%{_libdir}/jni/libcvc4compatjni.so*
%{_datadir}/java/CVC4compat.jar

%files doc
%defattr(-,root,root,-)
%{_datadir}/doc/cvc4/doxygen/html
%doc examples/README
%doc examples/*.c
%doc examples/*.java
%doc examples/*.cpp
%doc examples/*.py
%doc examples/*.php
%doc examples/*.pl
%doc examples/*.rb
%doc examples/*.tcl
%doc examples/*.ml

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%changelog
* Thu May 09 2013 Morgan Deters <mdeters@cs.nyu.edu> 1.2-1
* Wed Apr 03 2013 Morgan Deters <mdeters@cs.nyu.edu> 1.1-1
* Wed Feb 06 2013 Morgan Deters <mdeters@cs.nyu.edu> 1.0-1
- first attempt at a spec file for CVC4
